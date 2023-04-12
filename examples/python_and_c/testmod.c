#include <Python.h>
static PyObject *testmod_countchars(PyObject *self, PyObject *args)
{
  const char *text;
  int res;
  if (!PyArg_ParseTuple(args, "s", &text))
    return NULL;
  res = strlen(text);
  return Py_BuildValue("i", res);
}


static PyObject *testmod_countchars2(PyObject *self, PyObject *args, PyObject *keywords)
{
  const char *text;
  int other;
  int res;
  static char *kwlist[] = {"text", "other", NULL};
  if (!PyArg_ParseTupleAndKeywords(args, keywords, "si", kwlist, &text, &other))
    return NULL;
  res = strlen(text) + other;
  return Py_BuildValue("i", res);
}

static PyObject *testmod_countchars3(PyObject *self, PyObject *args, PyObject *keywords)
{
  const char *text;
  int other = 0;
  int res;
  static char *kwlist[] = {"text", "other", NULL};
  if (!PyArg_ParseTupleAndKeywords(args, keywords, "s|i", kwlist, &text, &other))
    return NULL;
  res = strlen(text) + other;
  return Py_BuildValue("i", res);
}


static PyMethodDef testmodMethods[] =
  {
    {
      "countchars",
      testmod_countchars,
      METH_VARARGS,
      "Count characters in the input string."
    },
    {
      "countchars2",
      (PyCFunction)testmod_countchars2,
      METH_VARARGS | METH_KEYWORDS,
      "Count characters in the input string and add 'other' value (keywords version)."
    },
    {
      "countchars3",
      (PyCFunction)testmod_countchars3,
      METH_VARARGS | METH_KEYWORDS,
      "Count characters in the input string and add 'other' value (keywords and default value version)."
    },
    { NULL, NULL, 0, NULL }
  };

static struct PyModuleDef testmod =
{
  PyModuleDef_HEAD_INIT,
  "testmod", 
  "Super module",          
  -1, // keep global variables
  testmodMethods
};

PyMODINIT_FUNC PyInit_testmod(void)
{
  return PyModule_Create(&testmod);
}
