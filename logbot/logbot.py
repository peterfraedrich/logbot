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

    def __init__(self, app_name='app.logbot'):
        '''
        @param app_name str
        instantiate a new instance of the logger
        '''
        self._log = logging.getLogger(app_name)
        return


    def configure(self, config_dict):
        '''
        @param config_dict dict
        set logging configurations
        '''
        logging.basicConfig(**config_dict)
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
            start = time.time()
            try:
                rtn = fn(*args, **kwargs)
            except Exception as e:
                ex = e
            msg = ''
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