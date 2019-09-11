#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PyobsException(Exception):
    pass


class ConnectionFailure(PyobsException):
    pass


class MessageTimeout(PyobsException):
    pass


class ObjectError(PyobsException):
    pass
