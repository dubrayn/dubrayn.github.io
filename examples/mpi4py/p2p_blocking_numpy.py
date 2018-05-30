#!/usr/bin/env python

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# passing MPI datatypes explicitly
if rank == 0:
  data = np.arange(1000, dtype = 'i')
  comm.Send([data, MPI.INT], dest = 1)
  print("send: %f" % (np.linalg.norm(data)))
elif rank == 1:
  data = np.empty(1000, dtype = 'i')
  comm.Recv([data, MPI.INT], source = 0)
  print("recv: %f" % (np.linalg.norm(data)))
