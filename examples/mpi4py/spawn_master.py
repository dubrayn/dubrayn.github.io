#!/usr/bin/env python

from mpi4py import MPI
import numpy
import sys

nbprocs = 100

comm = MPI.COMM_SELF.Spawn(sys.executable, args = ['spawn_slave.py'], maxprocs = nbprocs)

N = numpy.array(nbprocs, 'i')
comm.Bcast([N, MPI.INT], root = MPI.ROOT)
PI = numpy.array(0.0, 'd')
comm.Reduce(None, [PI, MPI.DOUBLE], op = MPI.SUM, root = MPI.ROOT)

print(PI)

comm.Disconnect()
