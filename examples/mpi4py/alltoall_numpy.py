#!/usr/bin/env python

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

sendbuf = np.arange(size, dtype = 'i') + rank * size
recvbuf = np.empty([size], dtype = 'i')

comm.Alltoall(sendbuf, recvbuf)

print("rank: %1d, recv: %s" % (rank, str(recvbuf)))
