cmake_minimum_required(VERSION 3.3 FATAL_ERROR)

project(vtk_hello_world)

find_package(VTK COMPONENTS 
  vtkCommonColor
  vtkCommonCore
  vtkFiltersSources
  vtkInteractionStyle
  vtkRenderingContextOpenGL2
  vtkRenderingCore
  vtkRenderingFreeType
  vtkRenderingGL2PSOpenGL2
  vtkRenderingOpenGL2 QUIET)
if (NOT VTK_FOUND)
  message("Skipping vtk_hello_world: ${VTK_NOT_FOUND_MESSAGE}")
  return ()
endif()
message (STATUS "VTK_VERSION: ${VTK_VERSION}")
if (VTK_VERSION VERSION_LESS "8.90.0")
  # old system
  include(${VTK_USE_FILE})
  add_executable(vtk_hello_world MACOSX_BUNDLE vtk_hello_world.cxx )
  target_link_libraries(vtk_hello_world PRIVATE ${VTK_LIBRARIES})
else ()
  # include all components
  add_executable(vtk_hello_world MACOSX_BUNDLE vtk_hello_world.cxx )
  target_link_libraries(vtk_hello_world PRIVATE ${VTK_LIBRARIES})
  # vtk_module_autoinit is needed
  vtk_module_autoinit(
    TARGETS vtk_hello_world
    MODULES ${VTK_LIBRARIES}
    )
endif () 

