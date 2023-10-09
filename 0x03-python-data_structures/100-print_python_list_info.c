#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - function that prints some basic info
 *				about Python lists
 * @p: the PyObject list
 *
 */

void print_python_list_info(PyObject *p)
{
	int size, i;
	PyObject *obj;

	size = Py_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
