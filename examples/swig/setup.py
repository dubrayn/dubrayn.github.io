from setuptools import setup, Extension

module1 = Extension('_testmod',
                    sources = ['testmod.i', 'myfunc0.c'])

setup (name = 'package_test',
       py_modules = ['testmod'],
       version = '1.0',
       description = 'This is a test package',
       ext_modules = [module1])

