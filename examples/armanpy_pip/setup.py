from setuptools import setup, Extension
from setuptools.command.build_py import build_py as _build_py

class build_py(_build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()

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
       cmdclass = {'build_py' : build_py},
       ext_modules = [module1])

