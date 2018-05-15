#!/usr/bin/env python

# generate 'mandel_image.vti' first !
import vtk

# source
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName('mandel_image.vti')
reader.Update()

# Set active scalars
pointData = reader.GetOutput().GetPointData()
pointData.SetActiveScalars('N')

# renderer
ren = vtk.vtkRenderer()

# window
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# interactor style
styleImage = vtk.vtkInteractorStyleImage()
styleImage.SetInteractionModeToImage3D()

# interactor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.SetInteractorStyle(styleImage)
iren.Initialize()

im = vtk.vtkImageResliceMapper()
im.SetInputConnection(reader.GetOutputPort())
im.SliceFacesCameraOn()
im.SliceAtFocalPointOn()
im.BorderOn()

ia = vtk.vtkImageSlice()
ia.SetMapper(im)

ren.AddActor(ia)
ren.SetBackground(1, 1, 1)

# set window size and render
renWin.SetSize(300, 300)
renWin.Render()

# start interactor loop
iren.Start()
