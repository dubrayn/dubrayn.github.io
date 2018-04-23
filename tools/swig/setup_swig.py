#from distutils.core import setup, Extension
from setuptools import setup, Extension

module1 = Extension('_testmod',
                    sources = ['swig_testmod.i', 'myfunc0.c'])

setup (name = 'TestPackage',
       version = '1.0',
       description = 'This is a test package',
       ext_modules = [module1])

