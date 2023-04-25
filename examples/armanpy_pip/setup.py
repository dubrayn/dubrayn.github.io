from setuptools import setup, Extension

module1 = Extension('_armanpypsa',
                    include_dirs = ['./armanpy/', 'src/'],
                    libraries = ['m', 'z', 'armadillo'],
                    sources = ['armanpypsa.i', 'src/myclass.cpp'],
                    swig_opts = ["-c++", "-Wall", "-I.", "-I./armanpy/", "-Isrc/"])

setup (name = 'armanpypsa',
       py_modules = ['armanpypsa'],
       version = '1.0',
       description = 'This is a test package',
       install_requires= ['numpy'],
       options = {"build_ext": {"inplace": False}},
       ext_modules = [module1])

