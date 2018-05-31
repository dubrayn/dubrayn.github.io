#!/usr/bin/env python

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

fp = MPI.File.Open(comm, "/tmp/test_mpiio.dat", MPI.MODE_WRONLY | MPI.MODE_CREATE)

buffer = np.zeros(16, dtype=np.int8)
buffer[0] = rank
buffer[1:16] = [ord(i) for i in 'string in ascii']
print(str(buffer))

offset = rank * buffer.nbytes
fp.Write_at_all(offset, buffer)

fp.Close()
