%module testclass

%{
#define SWIG_FILE_WITH_INIT

#include "testclass.h"
%}

%include "armanpy.i"

%include "testclass.h"
