%module testmod3
%{
#include "myclass.h"
%}

%include "exception.i"
%exception
{
  try
  {
    $action
  }
  catch (const std::runtime_error& e)
  {
    SWIG_exception(SWIG_RuntimeError, e.what());
  } 
  catch (const std::invalid_argument& e)
  {
    SWIG_exception(SWIG_ValueError, e.what());
  }
  catch (const std::out_of_range& e)
  {
    SWIG_exception(SWIG_IndexError, e.what());
  }
  catch (...)
  { 
    SWIG_exception(SWIG_RuntimeError, "unknown exception");
  } 
}

%include "myclass.h"
