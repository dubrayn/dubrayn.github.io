#!/usr/bin/env python

import multiprocessing

def worker(n):
  print('new worker: %d' % (n))

for i in range(8):
  multiprocessing.Process(target = worker, args = (i,)).start()

