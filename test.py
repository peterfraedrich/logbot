#!/usr/bin/env python

from __future__ import print_function
from functools import wraps
import time
from datetime import datetime
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger('logbot')

def logged(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        rtn = fn(*args, **kwargs)
        msg = '{}:{}.{}:params({}, {}):etime({})'.format(
                datetime.now(),
                fn.__name__,
                '__call__',
                args,
                kwargs,
                time.time() - start
            )
        print(msg)
        log.debug(msg)
        return rtn
    return wrapper



@logged
def something(hello):

    print(hello)

    return hello


something('whats up')