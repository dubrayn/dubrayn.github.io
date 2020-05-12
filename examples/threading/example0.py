#!/usr/bin/env python3

import threading

def worker():
  print('new worker')

for i in range(8):
  threading.Thread(target = worker).start()

