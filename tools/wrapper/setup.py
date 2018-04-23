from setuptools import setup, Extension

module1 = Extension('testmod',
                    sources = ['wrapper_testmod.c', 'myfunc0.c'])

setup (name = 'package_test',
       py_modules = ['testmod'],
       version = '1.0',
       description = 'This is a test package',
       ext_modules = [module1])

