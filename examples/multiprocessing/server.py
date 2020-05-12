#!/usr/bin/env python3
from multiprocessing.managers import BaseManager
import multiprocessing

queue = multiprocessing.Queue()
class QueueManager(BaseManager): pass
QueueManager.register('get_queue', callable=lambda:queue)
m = QueueManager(address=('', 50000), authkey=b'abracadabra')
s = m.get_server()
s.serve_forever()
