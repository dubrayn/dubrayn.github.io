#!/usr/bin/env python

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(threadName)s) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

s = threading.Event()
def worker(n):
  global s
  logging.debug("waiting for signal")
  s.wait()
  logging.debug("signal received")

logging.debug("start")
for i in range(3):
  threading.Thread(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()
logging.debug("send signal")
s.set()
