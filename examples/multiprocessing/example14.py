#!/usr/bin/env python

import logging
import multiprocessing
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(process)d) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

c = multiprocessing.Semaphore(2)
a = 0
def worker(n):
  global a
  logging.debug("wait")
  c.acquire()
  time.sleep(0.1)
  logging.debug("received !")
  c.release()
  logging.debug("release")

logging.debug("start")
for i in range(10):
  multiprocessing.Process(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()

