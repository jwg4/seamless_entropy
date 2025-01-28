#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include <Python.h>
#include <math.h>

#include <stdlib.h>
#include <stdbool.h>

#include "entropy.h"


static PyMethodDef NormieImplMethods[] =
{
     {"binary_entropy", binary_entropy, METH_VARARGS, "Entropy (with base 2 logs)"},
     {NULL, NULL, 0, NULL}
};

struct module_state {
	PyObject *error;
};

static int entropy_c_traverse(PyObject *m, visitproc visit, void *arg) {
	Py_VISIT(((struct module_state*)PyModule_GetState(m))->error);
	return 0;
}

static int entropy_c_clear(PyObject *m) {
	Py_CLEAR(((struct module_state*)PyModule_GetState(m))->error);
	return 0;
}

static struct PyModuleDef moduledef = {
	PyModuleDef_HEAD_INIT,
	"entropy_c",
	NULL,
	sizeof(struct module_state),
	NormieImplMethods,
	NULL,
	entropy_c_traverse,
	entropy_c_clear,
	NULL
};


/* module initialization */
PyMODINIT_FUNC
PyInit_entropy_c(void)
{
     PyObject *module = PyModule_Create(&moduledef);

     if (module == NULL)
	 return NULL;

     struct module_state *st = (struct module_state*)PyModule_GetState(module);

     return module;
}


