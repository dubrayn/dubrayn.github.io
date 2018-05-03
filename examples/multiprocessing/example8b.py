#!/usr/bin/env python

import logging
import multiprocessing
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(process)d) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def worker(n, a):
  b = a.value
  time.sleep(0.0001)
  a.value = b + 1
  logging.debug("worker %d: a = %d" % (n, a.value))

logging.debug("start")
a = multiprocessing.Value('i', 0)

for i in range(3):
  multiprocessing.Process(name = 'THREAD-%01d' % (i), target = worker, args = (i, a)).start()
