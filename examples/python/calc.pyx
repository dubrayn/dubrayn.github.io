#!/usr/bin/env python

import numpy as np
cimport numpy as np
DTYPE = np.float64
ctypedef np.float64_t DTYPE_t

cimport cython
@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def fill(int n0, int n1):
  cdef int i
  cdef int j
  cdef np.ndarray a = np.empty((n0, n1), dtype = DTYPE)
  cdef np.ndarray b = np.empty((n1, n0), dtype = DTYPE)
  cdef DTYPE_t value
  for i in range(n0):
    for j in range(n1):
      value = (i * 1.0 + j * 0.1) * 0.1
      a[i, j] = value
      b[j, i] = value
  return a, b

def calc(np.ndarray a, np.ndarray b):
  return np.linalg.norm(a.dot(b), ord = 'fro')

