#!/usr/bin/env python

import mpi4py.MPI as mpi

rank = mpi.COMM_WORLD.rank

result = mpi.COMM_WORLD.allreduce(rank, mpi.SUM)

print("rank: %1d, result: %d" % (rank, result))
