#!/usr/bin/env python

from functools import wraps
import time
from datetime import datetime
import logging
from sys import stdout

class AutoLogger:
    '''
    Automatically generates logs
    '''

    def __init__(self, app_name='app.logbot', config={}):
        '''
        @param app_name str
        instantiate a new instance of the logger
        '''
        logging.basicConfig(**config)
        self._log = logging.getLogger(app_name)
        return

    def autolog(self, fn):
        '''
        function decorator that catches exceptions
        and loggs function calls automatically
        TODO:
            - set msg format
            - clean up exception handling
            - ???
            - profit
        '''
        @wraps(fn)
        def wrapper(*args, **kwargs):
            self._log.debug('function({}):args({}):kwargs({})'.format(fn.__name__, args, kwargs))
            start = time.time()
            rtn = None
            try:
                rtn = fn(*args, **kwargs)
            except Exception as e:
                self._log.error('function({}):exception({})'.format(fn.__name__, e))
            self._log.debug('function({}):return({})'.format(fn.__name__, rtn))
            self._log.debug('function({}):execution_time_ms({})'.format(fn.__name__, round(float(time.time() - start), 8)))
            return rtn
        return wrapper


    ### public methods for user-supplied logging messages
    ### without calling logging.getLogger()
    def debug(self, msg):
        self._log.debug(msg)
        return


    def info(self, msg):
        self._log.info(msg)
        return


    def warn(self, msg):
        self._log.warn(msg)
        return


    def error(self, msg):
        self._log.error(msg)
        return