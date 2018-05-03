#!/usr/bin/env python

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(threadName)s) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def worker(n):
  logging.debug("worker %d" % (n))

logging.debug("start")
for i in range(3):
  threading.Timer(i + 1.0, worker, args = (i,)).start()
logging.debug("stop ?")
