#!/usr/bin/env python

import vtk

# source
reader = vtk.vtkXMLRectilinearGridReader()
reader.SetFileName('mandel_grid.vtr')

# mapper
mandelMapper = vtk.vtkDataSetMapper()
mandelMapper.SetInputConnection(reader.GetOutputPort())
mandelMapper.SetScalarModeToUsePointFieldData()
mandelMapper.SelectColorArray('N')

# actor
mandelActor = vtk.vtkActor()
mandelActor.SetMapper(mandelMapper)

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
ren.AddActor(mandelActor)

# set window size and render
renWin.SetSize(300, 300)
renWin.Render()

# start interactor loop
iren.Start()
