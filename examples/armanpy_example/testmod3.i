%module testmod3
%include "stl.i"
%include "std_map.i"
%include "std_string.i"
%include "std_vector.i"
%include "std_vectora.i"
%include "exception.i"

namespace std
{
  %template(map_string_int) map<string, int>;
  %template(map_string_double) map<string, double>;
  %template(map_string_string) map<string, string>;
}

%exception
{
  try
  {
    $action
  }
  catch (const std::runtime_error& e) {
    SWIG_exception(SWIG_RuntimeError, e.what());
  }
  catch (const std::logic_error& e) {
    SWIG_exception(SWIG_IndexError, e.what());
  }
  catch (const std::string s) {
    SWIG_exception(SWIG_RuntimeError, s.c_str());
  }
}


%{
#define SWIG_FILE_WITH_INIT
#include "myclass.h"
%}

%include "armanpy.i"

%include "myclass.h"
