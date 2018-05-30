#!/usr/bin/env python

import time
from mpi4py import MPI

time0 = time.time()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

time.sleep(rank)
if rank == 0:
  comm.Barrier()
else:
  comm.Barrier()

time1 = time.time()

print('rank: %d, elapsed time: %fs' % (rank, time1 - time0))
