#!/usr/bin/env python

import numpy as np
from pyevtk.hl import gridToVTK

def mandelbrot_set(X, Y, maxiter, horizon=2.0):
    C = X + Y[:, None]*1j
    N = np.zeros(C.shape, dtype=int)
    Z = np.zeros(C.shape, np.complex64)
    for n in range(maxiter):
        I = np.less(abs(Z), horizon)
        N[I] = n
        Z[I] = Z[I]**2 + C[I]
    N[N == maxiter-1] = 0
    return Z.transpose(), N.transpose()

nx = 800
ny = 600
x = np.linspace(-2.25, 0.75, nx, dtype=np.float32)
y = np.linspace(-1.25, 1.25, ny, dtype=np.float32)
z = np.linspace(0.0, 1.0, 1, dtype=np.float32)

Z, N = mandelbrot_set(x, y, 200, 2.0 ** 10)

filename = 'mandel_grid'
gridToVTK(filename, x, y, z, pointData = {'N': N.reshape((nx, ny, 1), order = 'C')})
print('%s.vtr generated' % (filename))

