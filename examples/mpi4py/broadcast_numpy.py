#!/usr/bin/env python

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
  data = np.arange(100, dtype = 'i')
else:
  data = np.empty(100, dtype = 'i')

comm.Bcast(data, root = 0)

print("rank: %1d, recv: %f" % (rank, np.linalg.norm(data)))
