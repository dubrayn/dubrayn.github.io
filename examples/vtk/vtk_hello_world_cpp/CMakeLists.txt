cmake_minimum_required(VERSION 2.8.5 FATAL_ERROR)
if(POLICY CMP0025)
  cmake_policy(SET CMP0025 NEW) # CMake 3.0
endif()
if(POLICY CMP0053)
  cmake_policy(SET CMP0053 NEW) # CMake 3.1
endif()

project (ENSIIE-PSA)

find_package(VTK 6.0 REQUIRED NO_MODULE) 

include(${VTK_USE_FILE})

add_executable(vtk_hello_world MACOSX_BUNDLE vtk_hello_world.cpp)
target_link_libraries(vtk_hello_world ${VTK_LIBRARIES})
