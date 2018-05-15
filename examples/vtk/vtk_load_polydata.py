#!/usr/bin/env python

# generate 'mandel_polydata.vtp' first !
import vtk

# source
reader = vtk.vtkXMLPolyDataReader()
reader.SetFileName('mandel_polydata.vtp')

# store output port
outputPort = reader.GetOutputPort()

# mapper
mandelMapper = vtk.vtkDataSetMapper()
mandelMapper.SetInputConnection(outputPort)
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
