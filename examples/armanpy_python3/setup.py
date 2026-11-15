import numpy
from setuptools import setup, Extension

# ==============================================================================
# ==============================================================================
# ==============================================================================

def get_env(key):
  try:
    v = os.environ[key]
  except:
    v = ''
  return v

# ==============================================================================
# ==============================================================================
# ==============================================================================

include_dirs = [get_env('PYTHON3_ROOT'),
                './include/armanpy/',
                numpy.get_include()
               ]

libraries = ['m', 'z', 'lapack', 'blas']

include_dirs = [d for d in include_dirs if d != ""]

module1 = Extension('_testmod3',
                    include_dirs = include_dirs,
                    library_dirs = [
                                    get_env('LAPACK_LIBDIR'),
                                    get_env('BLAS_LIBDIR'),
                                   ],
                    libraries = libraries,
                    sources = ['testmod3.i', 'myclass.cpp'],
                    extra_compile_args = ['-std=c++14', '-DARMA_DONT_USE_WRAPPER', '-DARMA_USE_LAPACK', '-DARMA_USE_BLAS'],
                    swig_opts = ["-c++", "-Wall", "-I.", "-I./include/armanpy/"])

# ==============================================================================
# ==============================================================================
# ==============================================================================

setup (name = 'package_test',
       py_modules = ['testmod3'],
       version = '1.0',
       description = 'This is a test package',
       ext_modules = [module1])
