#!/usr/bin/env python

import mpi4py.MPI as mpi

class point:
  def __init__(self, x0, y0):
    self.x = x0
    self.y = y0
  def __add__(self, p):
    return point(self.x + p.x, self.y + p.y)
  def __str__(self):
    return '(%d, %d)' % (self.x, self.y)

rank = mpi.COMM_WORLD.rank
print('%d' % (rank))
p1 = point(rank, rank + 1)
p2 = mpi.COMM_WORLD.allreduce(p1, mpi.SUM)
print(p2)
