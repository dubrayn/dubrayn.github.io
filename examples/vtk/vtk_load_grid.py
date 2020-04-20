#!/usr/bin/env python3

# generate 'mandel_grid.vtr' first !
import vtk

# source
reader = vtk.vtkXMLRectilinearGridReader()
reader.SetFileName('mandel_grid.vtr')

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
