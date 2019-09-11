#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
from collections import defaultdict
import hashlib
import json
import logging
import socket
from threading import Event, Lock, Thread
from typing import Dict, Tuple
import websocket

from . import events
from .base_classes import BaseRequest
from .exceptions import ConnectionFailure, MessageTimeout, ObjectError

LOG = logging.getLogger(__name__)


class Client(object):
    """
    Core class for using pyobs

    Simple usage:
        >>> from pyobs import Client, requests as obsrequests
        >>> client = Client("localhost", 4444, "secret")
        >>> client.connect()
        >>> client.execute(obsrequests.GetVersion()).obs_websocket_version
        u'4.1.0'
        >>> client.disconnect()

    For advanced usage, including events callback, see the 'samples' directory.
    """

    def __init__(self, host='localhost', port=4444, password=''):
        """
        Construct a new Client wrapper

        :param host: Hostname to connect to
        :param port: TCP Port to connect to (Default is 4444)
        :param password: Password for the websocket server (Leave this field
            empty if no auth enabled on the server)
        """
        # Incremental id
        self._id = 0
        self._id_lock = Lock()
        # Websocket client
        self._ws = None  # type: websocket.WebSocket
        # Event handler
        self._event_handler = EventHandler()
        # Response handler
        self._response_handler = ResponseHandler()
        # Server thread that will listen
        self._server_thread = None  # type: WSServer

        # Address and authentication
        self.host = host
        self.port = port
        self.password = password

    @property
    def _next_id(self):
        with self._id_lock:
            self._id += 1
            return self._id

    # Required for the ServerThread to be able to access
    @property
    def ws(self):
        return self._ws

    # Required for the ServerThread to be able to access
    @property
    def event_handler(self):
        return self._event_handler

    # Required for the ServerThread to be able to access
    @property
    def response_handler(self):
        return self._response_handler

    def connect(self, host=None, port=None):
        """
        Connect to the websocket server

        :return: Nothing
        """
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port

        if self._server_thread is not None:
            self._server_thread.stop()
            self._server_thread.join()

        try:
            self._ws = websocket.WebSocket()
            LOG.info("Connecting...")
            self._ws.connect("ws://{}:{}".format(self.host, self.port))
            LOG.info("Connected!")
            self._auth(self.password)
        except socket.error as e:
            raise ConnectionFailure(str(e))

        self._server_thread = WSServer(self)
        self._server_thread.start()

    def _auth(self, password):
        self.ws.send(json.dumps({
            "request-type": "GetAuthRequired",
            "message-id": str(self._next_id),
        }))
        result = json.loads(self.ws.recv())

        if result['status'] != 'ok':
            raise ConnectionFailure(result['error'])

        if result.get('authRequired'):
            secret = base64.b64encode(
                hashlib.sha256(
                    (password + result['salt']).encode('utf-8')
                ).digest()
            )
            auth = base64.b64encode(
                hashlib.sha256(
                    secret + result['challenge'].encode('utf-8')
                ).digest()
            ).decode('utf-8')

            self.ws.send(json.dumps({
                "request-type": "Authenticate",
                "message-id": str(self._next_id),
                "auth": auth,
            }))
            result = json.loads(self.ws.recv())

            if result['status'] != 'ok':
                raise ConnectionFailure(result['error'])

    def reconnect(self):
        """
        Restart the connection to the websocket server

        :return: Nothing
        """
        try:
            self.disconnect()
        except Exception:
            # TODO: Need to catch more precise exception
            pass
        self.connect()

    def disconnect(self):
        """
        Disconnect from websocket server

        :return: Nothing
        """
        LOG.info("Disconnecting...")
        if self._server_thread is not None:
            self._server_thread.stop()

        try:
            self.ws.close()
        except socket.error:
            pass

        if self._server_thread is not None:
            self._server_thread.join()
            self._server_thread = None

    def execute(self, req: BaseRequest):
        """
        Execute a request to the OBS server through the Websocket.

        :param req: Request to send to the server.
        :return: Request object populated with response data.
        """
        if not isinstance(req, BaseRequest):
            raise ObjectError("Call parameter is not a request object")

        message_id = self._next_id
        self._response_handler[message_id] = req

        payload = req.payload
        payload['message-id'] = str(message_id)
        LOG.debug("Sending message id {}: {}".format(message_id, payload))
        self._ws.send(json.dumps(payload))

        return self._response_handler[message_id]

    def register(self, func, event=None):
        """
        Register a new hook in the websocket client

        :param func: Callback function pointer for the hook
        :param event: Event (class from pyobs.events module) to trigger the
            hook on. Default is None, which means trigger on all events.
        :return: Nothing
        """
        self._event_handler.register(func, event)

    def unregister(self, func, event=None):
        """
        Unregister a new hook in the websocket client

        :param func: Callback function pointer for the hook
        :param event: Event (class from pyobs.events module) which triggered
            the hook on. Default is None, which means unregister this function
            for all events.
        :return: Nothing
        """
        self._event_handler.unregister(func, event)


class WSServer(Thread):
    """Websocket server that listens and routes incoming messages."""
    def __init__(self, client: Client):
        self._client = client
        self._running = True
        Thread.__init__(self, daemon=True)

    def stop(self):
        self._running = False

    def run(self):
        LOG.debug("Starting server.")
        while self._running:
            raw_msg = ""
            try:
                raw_msg = self._client.ws.recv()

                # Skipping empty receives (see Elektordi/obs-websocket-py#6)
                if not raw_msg:
                    continue

                message = json.loads(raw_msg)
                if 'update-type' in message:
                    LOG.debug("Received event: {}".format(message))
                    self._handle_event(message)
                elif 'message-id' in message:
                    LOG.debug("Received answer for id {}: {}".format(
                        message['message-id'], message))
                    self._handle_response(message)
                else:
                    LOG.warning("Unknown message: {}".format(message))

            except websocket.WebSocketConnectionClosedException:
                if self._running:
                    self._client.reconnect()
            except (ValueError, ObjectError) as e:
                LOG.warning("Invalid message: {} ({})".format(raw_msg, e))

        LOG.debug("Server closed.")

    def _handle_event(self, message: dict):
        name = message["update-type"]
        try:
            cls = getattr(events, name)
        except AttributeError:
            raise ObjectError("Invalid event type {}".format(name))
        else:
            self._client.event_handler.trigger(cls.from_message(message))

    def _handle_response(self, message: dict):
        self._client.response_handler.answer(message['message-id'], message)


class EventHandler(object):
    """
    EventManager holds a mapping that relates classes to a list of callbacks.
    """
    def __init__(self):
        self._callbacks_mapping = defaultdict(list)

    def _add(self, key, item):
        self._callbacks_mapping[key].append(item)

    def _remove(self, key, item):
        try:
            self._callbacks_mapping[key].remove(item)
        except ValueError:
            pass  # Nothing to remove
        else:
            # Keep the mapping clean of zero-length lists
            if len(self._callbacks_mapping[key]) == 0:
                del self._callbacks_mapping[key]

    def register(self, callback, trigger=None):
        """
        Register a new callback for the trigger specified.

        If None is specified as trigger, it registers the callback for every
        trigger.

        :param callback: Function to call when triggered
        :param trigger: Class of event that triggers the callback
        :return: Nothing
        """
        self._add(trigger, callback)

    def unregister(self, callback, trigger=None):
        """
        Unregister a callback for the trigger specified.

        If None is specified as trigger, it unregisters the callback for every
        trigger.

        :param callback: Function to stop calling when triggered
        :param trigger: Class of event that triggered the callback
        :return: Nothing
        """
        # Special case for trigger == None, need to remove from all lists
        if trigger is None:
            for trigger in self._callbacks_mapping:
                self._remove(trigger, callback)
        # Checking if trigger is already in the callbacks mapping prevents
        # creating empty lists with remove
        elif trigger in self._callbacks_mapping:
            self._remove(trigger, callback)

    def trigger(self, data):
        """
        Triggers the callbacks registered to the class of the provided object.

        :param data: Object that triggers the callbacks
        :return: Nothing
        """
        # Checking if type(data) is already in the callbacks mapping prevents
        # creating empty lists with the loop
        if type(data) in self._callbacks_mapping:
            for callback in self._callbacks_mapping[type(data)]:
                callback(data)
        if None in self._callbacks_mapping:
            for callback in self._callbacks_mapping[None]:
                callback(data)


class ResponseHandler(object):
    def __init__(self, timeout: float=60.0) -> None:
        self._responses = {}  # type: Dict[int, Tuple[Event, BaseRequest]]
        self._timeout = timeout
        self._lock = Lock()

    def __getitem__(self, message_id: int):
        with self._lock:
            if message_id not in self._responses:
                raise ValueError("The requested response does not belong to "
                                 "any of the current requests.")

            event, req = self._responses[message_id]

        if not event.wait(self._timeout):
            raise MessageTimeout("No answer for message {}".format(message_id))

        del self[message_id]

        return req

    def __setitem__(self, message_id: int, value: BaseRequest):
        with self._lock:
            self._responses[message_id] = (Event(), value)

    def __delitem__(self, message_id: int):
        with self._lock:
            del self._responses[message_id]

    def answer(self, message_id: int, message: dict):
        with self._lock:
            if message_id in self._responses:
                event, req = self._responses[message_id]
                req.answer(message)
                event.set()
