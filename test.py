#!/usr/bin/python

from __future__ import print_function
from logbot import AutoLogger
import logging
import sys

config = {
    'stream' : sys.stdout,
    'level' : logging.DEBUG
}

print('instantiating new logbot class')
log = AutoLogger(app_name='testapp', config=config)

@log.autolog
def test(a, b, c, d, *args, **kwargs):
    return 'hello world'

@log.autolog
def extest():
    raise TypeError('wat')
    return None


test('a', 'b', 'c', 'd', 'e', 'f', g='g', h='h')
extest()