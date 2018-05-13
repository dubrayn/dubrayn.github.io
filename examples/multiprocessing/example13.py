#!/usr/bin/env python

import logging
import multiprocessing
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(process)d) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

c = multiprocessing.Condition()
def worker(n):
  logging.debug("wait")
  c.acquire()
  c.wait()
  logging.debug("received !")
  c.release()

logging.debug("start")
for i in range(3):
  multiprocessing.Process(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()
logging.debug("set condition")

for i in range(3):
  time.sleep(1.0)
  c.acquire()
  logging.debug("notify one thread")
  c.notify()
  c.release()
