#!/usr/bin/env python3

import logging
import multiprocessing

logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(process)d) %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                   )

def worker(n):
  logging.debug('new worker: %d' % (n))

logging.debug("start")
for i in range(8):
  multiprocessing.Process(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()

