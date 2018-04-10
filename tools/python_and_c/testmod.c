#include <Python.h>

static PyObject *testmod_countchars(PyObject *self, PyObject *args)
{
  const char *text;
  int sts;

  if (!PyArg_ParseTuple(args, "s", &text))
    return NULL;

  sts = strlen(text);

  return Py_BuildValue("i", sts);
}

static PyMethodDef testmodMethods[] =
  {
    {
      "countchars",
      testmod_countchars,
      METH_VARARGS,
      "Count characters in the input string."
    },
    { NULL, NULL, 0, NULL }
  };

PyMODINIT_FUNC inittestmod(void)
{
  (void) Py_InitModule("testmod", testmodMethods);
}

