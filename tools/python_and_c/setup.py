from distutils.core import setup, Extension

module1 = Extension('testmod',
                    sources = ['testmod.c'])

setup (name = 'TestPackage',
       version = '1.0',
       description = 'This is a test package',
       ext_modules = [module1])

