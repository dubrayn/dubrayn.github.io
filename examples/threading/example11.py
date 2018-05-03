#!/usr/bin/env python

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(threadName)s) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

l = threading.RLock()
def worker(n):
  logging.debug("lock.acquire()")
  l.acquire()
  logging.debug(" lock acquired !")
  logging.debug("  lock.acquire() again ?")
  l.acquire()
  logging.debug("   lock acquired !")
  logging.debug("    lock.release()")
  try:
    while True:
      l.release()
  except:
    pass
  logging.debug("     lock released !")

logging.debug("start")
for i in range(3):
  threading.Thread(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()
