#!/usr/bin/env python

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = (rank + 1)**2
data = comm.gather(data, root = 0)

print("rank: %1d, recv: %s" % (rank, str(data)))
