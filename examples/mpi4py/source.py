#!/usr/bin/env python

from mpi4py import MPI
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
  for i in range(1, size):
    data = comm.recv(source = i)
    print(data)
  for i in range(1, size):
    data = comm.recv(source = MPI.ANY_SOURCE)
    print(data)
else:
  data = 'Hello from rank %d' % (rank)
  comm.send(data, dest = 0)
  time.sleep(random.random())
  comm.send(data, dest = 0)
