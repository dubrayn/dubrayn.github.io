#!/usr/bin/env python

import logging
import multiprocessing
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(threadName)s) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

a = 0
def worker(n):
  global a
  b = a
  time.sleep(0.0001)
  a = b + 1
  logging.debug("worker %d: a = %d" % (n, a))

logging.debug("start")
for i in range(3):
  multiprocessing.Process(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()
