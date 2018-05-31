#!/usr/bin/env python

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = [(i + 1)**2 for i in range(size)]
else:
    data = None

data = comm.scatter(data, root = 0)

print("rank: %1d, recv: %s" % (rank, str(data)))
