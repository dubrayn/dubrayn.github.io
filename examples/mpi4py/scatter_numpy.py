#!/usr/bin/env python

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

sendbuf = None
if rank == 0:
  sendbuf = np.empty([size, 100], dtype = 'i')
  sendbuf.T[:, :] = range(size)

recvbuf = np.empty(100, dtype = 'i')

comm.Scatter(sendbuf, recvbuf, root = 0)

print("rank: %1d, recv: %f" % (rank, np.linalg.norm(recvbuf)))
