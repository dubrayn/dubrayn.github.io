#!/usr/bin/env python

import mpi4py.MPI as mpi
import numpy as np

rank = mpi.COMM_WORLD.rank

sendbuf = np.zeros([1], dtype = 'i') + rank
recvbuf = np.empty([1], dtype = 'i')

mpi.COMM_WORLD.Allreduce(sendbuf, recvbuf, mpi.SUM)

print("rank: %1d, result: %d" % (rank, recvbuf[0]))
