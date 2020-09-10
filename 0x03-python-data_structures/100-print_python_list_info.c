#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: the list of python
 *
 * Return: na
*/
void print_python_list_info(PyObject *p)
{
	int size_p = (int)PyList_Size(p), i;
	char *str = NULL;

	if (p == NULL)
	{
		return;
	}

	printf("[*] Size of the Python List = %d\n", size_p);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

	for (i = 0; i < size_p; i++)
	{
		str = (char *)PyList_GET_ITEM(p, i)->ob_type->tp_name;
		printf("Element %d: %s\n", i, str);
	}
}
