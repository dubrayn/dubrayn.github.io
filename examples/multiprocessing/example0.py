#!/usr/bin/env python

import multiprocessing

def worker():
  print('new worker')

for i in range(8):
  multiprocessing.Process(target = worker).start()

