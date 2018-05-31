#!/usr/bin/env python

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

sendbuf = np.zeros(5, dtype = 'i') + rank
recvbuf = np.empty([size, 5], dtype = 'i')

comm.Allgather(sendbuf, recvbuf)

print("rank: %1d, recv: %s" % (rank, str(recvbuf)))
