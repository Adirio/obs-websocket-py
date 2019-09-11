#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import copy


class _Base(object):
    def __init__(self):
        self._name = '?'
        self._returns = {}

    def __getitem__(self, item):
        return self._returns[item]

    @property
    def name(self):
        """Name of the event or request."""
        return self._name

    def _fill_returns(self, data):
        self._returns = copy(data)


class BaseEvent(_Base):
    def __repr__(self):
        return "<{} event ({})>".format(self._name, self._returns)

    @classmethod
    def from_message(cls, data):
        """
        Returns a new event instance with the data from a websocket message

        :param data: websocket message data
        :return: event instance
        """
        obj = cls()
        obj._fill_returns(data)
        return obj

    def _fill_returns(self, data):
        del data['update-type']
        _Base._fill_returns(self, data)


class BaseRequest(_Base):
    def __init__(self):
        _Base.__init__(self)
        self._params = {}
        self._status = None

    def __repr__(self):
        if self._status is None:
            return "<{} request ({}) waiting>".format(self._name, self._params)
        elif self._status:
            return "<{} request ({}) called: success ({})>".format(
                self._name, self._params, self._returns)
        else:
            return "<{} request ({}) called: failed ({})>".format(
                self._name, self._params, self._returns)

    @property
    def payload(self):
        """
        Prepares the websocket message.

        :return: prepared websocket message
        """
        payload = copy(self._params)
        payload.update({'request-type': self._name})
        return payload

    def answer(self, data):
        """
        Fill the response answer of a request from a websocket message.

        :param data: websocket message data
        :return: Nothing
        """
        self._fill_returns(data)

    def _fill_returns(self, data):
        self._status = data['status'] == 'ok'
        del data['status']
        del data['message-id']
        _Base._fill_returns(self, data)
