#!/usr/bin/env python

from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
  time.sleep(0.3)
  data = 'Hello COMM_WORLD !'
  req = comm.send(data, dest = 1)
elif rank == 1:
  req = comm.irecv(source = 0)
  flag, data = req.test()
  if not flag:
    req.Cancel()
    print("cancelled")
  req = comm.irecv(source = 0)
  flag, data = req.test()
  while not flag:
    print("waiting (irecv)")
    time.sleep(0.5)
    flag, data = req.test()
  print("Received '%s'" % (data))
