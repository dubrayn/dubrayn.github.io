#!/usr/bin/env python

import logging
import multiprocessing
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(process)d) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def worker(n, a, l):
  logging.debug("lock.acquire()")
  l.acquire()
  logging.debug(" lock acquired !")
  b = a.value
  time.sleep(0.2)
  a.value = b + 1
  logging.debug("  worker %d: a = %d" % (n, a.value))
  logging.debug("   lock.release()")
  l.release()
  logging.debug("    lock released !")

logging.debug("start")
lock = multiprocessing.Lock()
a = multiprocessing.Value('i', 0, lock = False)

for i in range(3):
  multiprocessing.Process(name = 'THREAD-%01d' % (i), target = worker, args = (i, a, lock)).start()
