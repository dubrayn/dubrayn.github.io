#!/usr/bin/env python3

import logging
import threading

logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(threadName)s) %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                   )

def worker(n):
  logging.debug('new worker: %d' % (n))

logging.debug("start")
for i in range(8):
  threading.Thread(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()

