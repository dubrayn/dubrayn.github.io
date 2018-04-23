#include <Python.h>
#include "myfunc0.h"

static PyObject *testmod_myfunc0(PyObject *self, PyObject *args)
{
  double x, result;
  if (!PyArg_ParseTuple(args, "d", &x))
  {
    return NULL;
  }

  result = myfunc0(x);

  return Py_BuildValue("d", result);
}

static PyMethodDef testmodMethods[] =
  {
    {
      "myfunc0",
      testmod_myfunc0,
      METH_VARARGS,
      "Calculate x * x + 1."
    },
    { NULL, NULL, 0, NULL }
  };

PyMODINIT_FUNC inittestmod(void)
{
  (void) Py_InitModule("testmod", testmodMethods);
}

