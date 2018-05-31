#!/usr/bin/env python

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

sendbuf = np.zeros(5, dtype = 'i') + rank
recvbuf = None
if rank == 0:
  recvbuf = np.empty([size, 5], dtype = 'i')

comm.Gather(sendbuf, recvbuf, root = 0)

print("rank: %1d, recv: %s" % (rank, str(recvbuf)))
