#!/usr/bin/env python

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# automatic MPI datatype discovery
if rank == 0:
  data = np.arange(100, dtype = np.float64)
  comm.Send(data, dest = 1)
  print("send: %f" % (np.linalg.norm(data)))
elif rank == 1:
  data = np.empty(100, dtype = np.float64)
  req = comm.Irecv(data, source = 0)
  req.Wait()
  print("recv: %f" % (np.linalg.norm(data)))
