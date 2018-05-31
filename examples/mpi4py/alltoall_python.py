#!/usr/bin/env python

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = [i + rank * size for i in range(size)]

data = comm.alltoall(data)

print("rank: %1d, recv: %s" % (rank, str(data)))
