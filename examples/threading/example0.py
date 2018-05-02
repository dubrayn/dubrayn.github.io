#!/usr/bin/env python

import threading

def worker():
  print('new worker')

for i in range(8):
  threading.Thread(target = worker).start()

