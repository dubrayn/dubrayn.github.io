#!/usr/bin/env python

import numpy as np
import vtk

def mandelbrot_set(X, Y, maxiter, horizon=2.0):
  C = X + Y[:, None]*1j
  N = np.zeros(C.shape, dtype=int)
  Z = np.zeros(C.shape, np.complex64)
  for n in range(maxiter):
    if n % (maxiter / 10) == 0:
      print('progress: %d/%d' % (n, maxiter))
    I = np.less(abs(Z), horizon)
    N[I] = n
    Z[I] = Z[I]**2 + C[I]
  N[N == maxiter-1] = 0
  return Z.transpose(), N.transpose()

nx = 800
ny = 600
x = np.linspace(-2.25, 0.75, nx, dtype=np.float32)
y = np.linspace(-1.25, 1.25, ny, dtype=np.float32)

Z, N = mandelbrot_set(x, y, 2000, 2.0 ** 40)

filename = 'mandel_polydata'

points = vtk.vtkPoints()
vertices = vtk.vtkCellArray()

d0 = vtk.vtkFloatArray()
d0.SetName('N')
d0.SetNumberOfTuples(nx * ny)
d0.SetNumberOfComponents(1)

n = 0
for ix, vx in enumerate(x):
  if ix % (nx / 10) == 0:
    print('saving: %d/%d' % (ix, nx))

  for iy, vy in enumerate(y):
    id = points.InsertNextPoint(vx, vy, 0)
    d0.SetComponent(n, 0, N[(ix, iy)])
    vertices.InsertNextCell(1)
    vertices.InsertCellPoint(id)
    n += 1

polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.GetPointData().AddArray(d0)
polydata.GetPointData().SetScalars(d0)
polydata.SetVerts(vertices)

delaunay = vtk.vtkDelaunay2D()
delaunay.SetInputData(polydata)
delaunay.Update()

writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName('%s.vtp' % (filename))
writer.SetInputData(delaunay.GetOutput())
writer.Write()

print('%s.vtp generated' % (filename))
