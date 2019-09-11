#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from threading import Event, Lock
from typing import Dict, Tuple

from .base_classes import BaseRequest
from .exceptions import MessageTimeout


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
