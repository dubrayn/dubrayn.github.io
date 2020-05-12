#!/usr/bin/env python3

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(threadName)s) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

l = threading.Lock()
a = 0
def worker(n):
  global a
  logging.debug("lock.acquire()")
  l.acquire()
  logging.debug(" lock acquired !")
  b = a
  time.sleep(0.0001)
  a = b + 1
  logging.debug("  worker %d: a = %d" % (n, a))
  logging.debug("   lock.release()")
  l.release()
  logging.debug("    lock released !")

logging.debug("start")
for i in range(3):
  threading.Thread(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()
