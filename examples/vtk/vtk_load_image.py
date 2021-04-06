#!/usr/bin/env python3

# generate 'mandel_image.vti' first !
import vtk

# source
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName('mandel_image.vti')
reader.Update()

# Set active scalars
pointData = reader.GetOutput().GetPointData()
pointData.SetActiveScalars('N')

# mapper
mapper = vtk.vtkDataSetMapper()
mapper.SetInputConnection(reader.GetOutputPort())
mapper.SetScalarRange(0.0, 40.0)

# actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# renderer
ren = vtk.vtkRenderer()
ren.AddActor(actor)
ren.SetBackground(0, 0, 0)

# window
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# interactor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()

# set window size and render
renWin.SetSize(300, 300)
renWin.Render()

# start interactor loop
iren.Start()
