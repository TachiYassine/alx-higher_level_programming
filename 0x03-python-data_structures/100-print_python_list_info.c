#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - print basic info about python lists.
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	print("[*] size of the Python List = %d\n", size);
	print("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		print("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
