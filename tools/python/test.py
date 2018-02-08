#!/usr/bin/env python

import sys
import time
import numpy as np
import testclass

n0 = 2000
n1 = 2000 

print("===== Pythran =====")
time0 = time.time()
import matrix_multiply
time1 = time.time()
A = [[((i + j * 0.1) * 0.1) for i in xrange(n0)] for j in xrange(n1)]
B = [[((j + i * 0.1) * 0.1) for i in xrange(n0)] for j in xrange(n1)]
time2 = time.time()
mat = matrix_multiply.matrix_multiply(A, B)
time3 = time.time()
N = np.linalg.norm(mat, ord = 'fro')
time4 = time.time()
print("init. time: %fs" % (time1 - time0))
print("fill. time: %fs" % (time2 - time1))
print("mult. time: %fs" % (time3 - time2))
print("norm. time: %fs" % (time4 - time3))
print("TOTAL time: %fs" % (time4 - time0))
print("result    : %20.14e" % (N))

print("===== Numpy 1a =====")
time0 = time.time()
A = np.empty((n0, n1))
B = np.empty((n1, n0))
for i in range(n0):
  for j in range(n1):
    A[i, j] = (i + j * 0.1) * 0.1
    B[j, i] = (i + j * 0.1) * 0.1

time1 = time.time()
N = np.linalg.norm(A.dot(B), ord = 'fro')
time2 = time.time()

print("fill. time: %fs" % (time1 - time0))
print("calc. time: %fs" % (time2 - time1))
print("total time: %fs" % (time2 - time0))
print("result    : %20.14e" % (N))

print("===== Numpy 1b =====")
time0 = time.time()
A = np.empty((n0, n1))
for i in range(n0):
  for j in range(n1):
    A[i, j] = (i + j * 0.1) * 0.1
B = A.transpose()

time1 = time.time()
N = np.linalg.norm(A.dot(B), ord = 'fro')
time2 = time.time()

print("fill. time: %fs" % (time1 - time0))
print("calc. time: %fs" % (time2 - time1))
print("total time: %fs" % (time2 - time0))
print("result    : %20.14e" % (N))

print("===== Numpy 2 =====")
time0 = time.time()
A = np.empty((n0, n1))
it = np.nditer(A, flags = ['multi_index'],
               op_flags = ['writeonly'])
while not it.finished:
  it[0] = (it.multi_index[0]
          + it.multi_index[1] * 0.1) * 0.1
  it.iternext()
B = A.transpose()  

time1 = time.time()
N = np.linalg.norm(A.dot(B), ord = 'fro')
time2 = time.time()

print("fill. time: %fs" % (time1 - time0))
print("calc. time: %fs" % (time2 - time1))
print("total time: %fs" % (time2 - time0))
print("result    : %20.14e" % (N))

print("===== Numpy 3 =====")
time0 = time.time()
im, jm = np.mgrid[0:n0, 0:n1]
A = (im + jm * 0.1) * 0.1
B = A.transpose()  

time1 = time.time()
N = np.linalg.norm(A.dot(B), ord = 'fro')
time2 = time.time()
print("fill. time: %fs" % (time1 - time0))
print("calc. time: %fs" % (time2 - time1))
print("total time: %fs" % (time2 - time0))
print("result    : %20.14e" % (N))

print("===== Numba =====")
time0 = time.time()
from numba import jit

@jit
def fill(n0, n1):
  a = np.empty((n0, n1))
  for i in range(n0):
    for j in range(n1):
      a[i, j] = (i + j * 0.1) * 0.1
  b = a.transpose()
  return a, b

@jit
def calc(a, b):
  return np.linalg.norm(a.dot(b), ord = 'fro')

time1 = time.time()
A, B = fill(n0, n1) 
time2 = time.time()
N = calc(A, B)
time3 = time.time()
print("comp. time: %fs" % (time1 - time0))
print("fill. time: %fs" % (time2 - time1))
print("calc. time: %fs" % (time3 - time2))
print("TOTAL time: %fs" % (time3 - time0))
print("result    : %20.14e" % (N))

print("===== Cython =====")
time0 = time.time()
import calc
time1 = time.time()
A, B = calc.fill(n0, n1)
time2 = time.time()
N = calc.calc(A, B)
time3 = time.time()
print("init. time: %fs" % (time1 - time0))
print("fill. time: %fs" % (time2 - time1))
print("calc. time: %fs" % (time3 - time2))
print("TOTAL time: %fs" % (time3 - time0))
print("result    : %20.14e" % (N))

print("===== Armadillo =====")
time0 = time.time()
c = testclass.TestClass(n0, n1)
time1 = time.time()
c.init0()
time2 = time.time()
N = c.func0()
time3 = time.time()
print("init. time: %fs" % (time1 - time0))
print("fill. time: %fs" % (time2 - time1))
print("calc. time: %fs" % (time3 - time2))
print("TOTAL time: %fs" % (time3 - time0))
print("result    : %20.14e" % (N))

print("===== Armadillo 2 =====")
time0 = time.time()
c = testclass.TestClass(n0, n1)
time1 = time.time()
c.init1()
time2 = time.time()
N = c.func0()
time3 = time.time()
print("init. time: %fs" % (time1 - time0))
print("fill. time: %fs" % (time2 - time1))
print("calc. time: %fs" % (time3 - time2))
print("TOTAL time: %fs" % (time3 - time0))
print("result    : %20.14e" % (N))

