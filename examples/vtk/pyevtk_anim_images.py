#!/usr/bin/env python

import numpy as np
from evtk.hl import imageToVTK

def gen_image(x, y, t):
  xm, ym = np.meshgrid(x, y)
  d = np.power(xm, 2) + np.power(ym, 2)
  return np.cos( np.sqrt(d) * 2.0 - t) / (1.0 + d)
  

nx = 101
ny = 101
nt = 30
x = np.linspace(-10.0, 10.0, nx, dtype=np.float32)
y = np.linspace(-10.0, 10.0, ny, dtype=np.float32)
t = np.linspace(0, 2 * np.pi, nt, dtype=np.float32)

for it, vt in enumerate(t):
  N = gen_image(x, y, vt)
  filename = 'anim_%04d' % it
  imageToVTK(filename, pointData = {'N': N.astype(np.float32).reshape((nx, ny, 1), order = 'C')})
  print('%s.vti generated' % (filename))
