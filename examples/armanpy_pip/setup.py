from setuptools import setup, Extension

#===============================================================================
#===============================================================================
#===============================================================================

# fix an annoying bug with setuptools
# https://stackoverflow.com/questions/29477298/setup-py-run-build-ext-before-anything-else/48942866#48942866

from setuptools.command.build_py import build_py as _build_py

class build_py(_build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()

#===============================================================================
#===============================================================================
#===============================================================================

module1 = Extension('_armanpypsa',
                    include_dirs = ['./armanpy/', 'src/', '/opt/python/cp310-cp310/lib/python3.10/site-packages/numpy/core/include/'],
                    libraries = ['m', 'z', 'armadillo'],
                    sources = ['armanpypsa.i', 'src/myclass.cpp'],
                    swig_opts = ["-c++", "-Wall", "-I.", "-I./armanpy/", "-Isrc/"])

#===============================================================================
#===============================================================================
#===============================================================================

setup (name = 'armanpypsa',
       py_modules = ['armanpypsa'],
       version = '1.0',
       description = 'This is a test package',
       # install_requires= ['numpy'],
       options = {"build_ext": {"inplace": False}},
       cmdclass = {'build_py' : build_py}, # <= fix for the bug
       ext_modules = [module1])

