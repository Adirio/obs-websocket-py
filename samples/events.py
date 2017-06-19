#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, events

host = "localhost"
port = 4444
password = "secret"

def on_event(message):
    print "Got message: %r"%(message)
    if isinstance(message, events.SwitchScenes):
        print "You changed the scene to %s"%(message.getSceneName())

ws = obsws(host, port, password)
ws.register(on_event)
ws.connect()

try:
    print "OK"
    time.sleep(10)
    print "END"

except KeyboardInterrupt:
    pass

ws.disconnect()