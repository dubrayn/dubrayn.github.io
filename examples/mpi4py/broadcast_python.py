#!/usr/bin/env python

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'school' : 'ENSIIE', 'numbers': [2 + 1j, 3.1415]}
else:
    data = None

data = comm.bcast(data, root = 0)
print("rank: %1d, recv: %s" % (rank, str(data)))
