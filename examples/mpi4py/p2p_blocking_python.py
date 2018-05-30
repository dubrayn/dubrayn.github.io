#!/usr/bin/env python

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
  data = 'Hello COMM_WORLD !'
  comm.send(data, dest = 1)
elif rank == 1:
  data = comm.recv(source = 0)
  print("Received '%s'" % (data))
