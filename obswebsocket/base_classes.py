#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy


class BaseEvent:
    def __init__(self):
        self._name = '?'
        self._returns = {}

    def input(self, data):
        r = copy.copy(data)
        del r['update-type']
        self._returns = r

    def __repr__(self):
        return "<{} event ({})>".format(self._name, self._returns)


class BaseRequest:
    def __init__(self):
        self._name = '?'
        self._params = {}
        self._returns = {}
        self._status = None

    def data(self):
        payload = copy.copy(self._params)
        payload.update({'request-type': self._name})
        return payload

    def input(self, data):
        r = copy.copy(data)
        del r['message-id']
        self._status = (r['status'] == 'ok')
        del r['status']
        self._returns = r

    def __repr__(self):
        if self._status is None:
            return "<{} request ({}) waiting>".format(self._name, self._params)
        elif self._status:
            return "<{} request ({}) called: success ({})>".format(
                self._name, self._params, self._returns)
        else:
            return "<{} request ({}) called: failed ({})>".format(
                self._name, self._params, self._returns)
