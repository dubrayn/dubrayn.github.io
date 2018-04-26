#!/usr/bin/env python

try:
  print('press Ctrl-C')
  while True:
    pass
except KeyboardInterrupt:
  print('SIGINT received')

