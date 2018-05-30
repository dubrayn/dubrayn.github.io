#!/usr/bin/env python

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
  data = 'Hello COMM_WORLD !'
  req = comm.isend(data, dest = 1)
  req.wait()
elif rank == 1:
  req = comm.irecv(source = 0)
  data = req.wait()
  print("Received '%s'" % (data))
