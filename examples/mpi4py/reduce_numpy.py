#!/usr/bin/env python

import mpi4py.MPI as mpi
import numpy as np

rank = mpi.COMM_WORLD.rank

sendbuf = np.zeros([1], dtype = 'i') + rank

recvbuf = None
if rank == 0:
  recvbuf = np.empty([1], dtype = 'i')

mpi.COMM_WORLD.Reduce(sendbuf, recvbuf, mpi.SUM, root = 0)

if rank == 0:
  print("rank: %1d, result: %d" % (rank, recvbuf[0]))
