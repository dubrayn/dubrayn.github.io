#!/usr/bin/env python

import logging
import multiprocessing
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(threadName)s) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def worker(n):
  time.sleep(1.0)

for i in range(3):
  multiprocessing.Process(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()

logging.debug(str([t.name for t in multiprocessing.enumerate()]))

