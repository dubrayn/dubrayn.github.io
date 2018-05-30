#!/usr/bin/env python

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

comm2 = comm.Split(color = rank / 4)
rank2 = comm2.Get_rank()

print('global rank: %02d local rank: %02d' % (rank, rank2))
