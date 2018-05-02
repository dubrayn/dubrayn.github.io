#!/usr/bin/env python

import threading
import time

def worker():
  print('new worker')
  time.sleep(0.5)
  print('end of worker')

t0 = threading.Thread(target = worker)
t1 = threading.Thread(target = worker)
t0.daemon = t1.daemon = True

print('before')
t0.start()
time.sleep(0.1)
t1.start()
print('after')
t0.join()
