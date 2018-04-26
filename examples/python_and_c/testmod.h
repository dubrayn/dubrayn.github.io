#ifndef TESTMOD_H
#define TESTMOD_H

static PyObject *testmod_countchars(PyObject *self, PyObject *args);
static PyObject *testmod_countchars2(PyObject *self, PyObject *args, PyObject *keywords);
static PyObject *testmod_countchars3(PyObject *self, PyObject *args, PyObject *keywords);
PyMODINIT_FUNC inittestmod(void);

#endif
