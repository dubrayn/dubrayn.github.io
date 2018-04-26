#!/usr/bin/env python

import os
from distutils.core import setup, Extension
from distutils.cmd import Command
testclass_dir = "."

extra_compile_args = []
try:
  extra_compile_args = ['-O3', '-march=native', '-DARMA_NO_DEBUG', '-std=c++11', os.environ['ARMADILLO_CXXFLAGS']]
#  extra_compile_args = ['-g', '-O0', '-march=native', '-DARMA_NO_DEBUG', '-std=c++11', os.environ['ARMADILLO_CXXFLAGS']]
except:
  pass

include_dirs = [testclass_dir ,'/usr/include/python2', '/usr/include', '../../deps/msgpack-c/include', './include/armanpy/']
try:
  include_dirs = [testclass_dir, os.environ['PYTHON_ROOT'] + '/include', '../../deps/msgpack-c/include', './include/armanpy/']
except:
  pass

testclass = Extension('_testclass', ['testclass.i'],
                include_dirs = include_dirs,
                libraries = ['m', 'z', 'armadillo'],
                extra_compile_args = extra_compile_args,
                extra_objects = [testclass_dir + '/libtestclass.so'],
                depends = [testclass_dir + '/libtestclass.so']
                )

setup(
    name = 'testclass',
    version = '0.1b',
    author = 'N. Dubray',
    description = """test function""",
    ext_modules = [ testclass ],
    py_modules = [ 'testclass' ],
)
