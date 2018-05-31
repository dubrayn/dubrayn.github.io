#!/usr/bin/env python

from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# automatic MPI datatype discovery
if rank == 0:
  data = np.arange(100, dtype = np.float64)
  time.sleep(0.2)
  comm.Send(data, dest = 1)
  print("send: %f" % (np.linalg.norm(data)))
elif rank == 1:
  data = np.empty(100, dtype = np.float64)
  req = comm.Irecv(data, source = 0)
  if not req.Test():
    req.Cancel()
    print("cancelled")
    req = comm.Irecv(data, source = 0)
  while not req.Test():
    print("waiting (irecv)")
    time.sleep(0.1)
  print("recv: %f" % (np.linalg.norm(data)))
