#!/usr/bin/env python3

import threading

def worker(n):
  print('new worker: %d' % (n))

for i in range(8):
  threading.Thread(target = worker, args = (i,)).start()

