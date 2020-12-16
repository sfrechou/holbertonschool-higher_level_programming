#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: PyObject List
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p) - 1;
	int index, alloc;
	PyObject *item;

	printf("[*] Size of the Python List = %i\n", size);

	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", alloc);

	for (index = 0; index < size; index++)
	{
		item = PyList_GetItem(p, index);
		printf("Element %d: ", index);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}

