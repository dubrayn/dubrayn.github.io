#!/usr/bin/env python

import vtk

# source
cylinder = vtk.vtkCylinderSource()

# mapper
cylinderMapper = vtk.vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

# actor
cylinderActor = vtk.vtkActor()
cylinderActor.SetMapper(cylinderMapper)
cylinderActor.RotateX(30.0)

# renderer
ren = vtk.vtkRenderer()

# window
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# interactor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()

# add actor to renderer
ren.AddActor(cylinderActor)

# set window size and render
renWin.SetSize(300, 300)
renWin.Render()

# start interactor loop
iren.Start()
