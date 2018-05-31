#!/usr/bin/env python

import mpi4py.MPI as mpi

rank = mpi.COMM_WORLD.rank

result = mpi.COMM_WORLD.reduce(rank, mpi.SUM, root = 0)

print("rank: %1d, result: %s" % (rank, str(result)))
