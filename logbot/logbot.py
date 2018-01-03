#!/usr/bin/env python

from functools import wraps
import time
from datetime import datetime
import logging
from sys import stdout
from collections import defaultdict
from decimal import Decimal, ROUND_UP

class AutoLogger:
    '''
    Automatically generates logs
    '''

    FORMAT = 'AUTOLOG:function({d[fn]}):args({d[arg]}):kwargs({d[kwarg]}):ex_time_ms({d[xtime]}):return({d[return]}):exception({d[exception]})'

    def __init__(self, app_name='app.logbot', config={}):
        '''
        @param app_name str
        instantiate a new instance of the logger
        '''
        logging.basicConfig(**config)
        self._log = logging.getLogger(app_name)
        return

    def _format(self, **kwargs):
        d = defaultdict(str, **kwargs)
        return str(self.FORMAT).format(d=defaultdict(str, **kwargs))

    def _xtime(self, start):
        start = Decimal(str(start)).quantize(Decimal('.000001'), rounding=ROUND_UP)
        end = Decimal(str(time.time())).quantize(Decimal('.000001'), rounding=ROUND_UP)
        return end - start

    def setformat(self, format_str):
        self.FORMAT = format_str
        return

    def autolog(self, fn):
        '''
        function decorator that catches exceptions
        and loggs function calls automatically
        '''
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.time()
            rtn = None
            try:
                rtn = fn(*args, **kwargs)
            except Exception as e:
                self._log.error(self._format(fn=fn.__name__, xtime=self._xtime(start), rtn=str(rtn), exception=str(e), arg=args, kwarg=kwargs))
                return e
            self._log.debug(self._format(fn=fn.__name__, xtime=self._xtime(start), rtn=str(rtn), arg=args, kwarg=kwargs))
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
