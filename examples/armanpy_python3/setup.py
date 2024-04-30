import numpy
from setuptools import setup, Extension

module1 = Extension('_testmod3',
                    include_dirs = ['./include/armanpy/', numpy.get_include()],
                    libraries = ['m', 'z', 'armadillo'],
                    sources = ['testmod3.i', 'myclass.cpp'],
                    swig_opts = ["-c++", "-Wall", "-I.", "-I./include/armanpy/"])

setup (name = 'package_test',
       py_modules = ['testmod3'],
       version = '1.0',
       description = 'This is a test package',
       ext_modules = [module1])

