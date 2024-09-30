#include <Python.h>

/* betty style doc for function print_python_list goes there */
/**
 * print_python_list - Entry point
 *
 * @p: first arg
 * Return: void
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, allocated, i;
    PyObject *item;

    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}

/* betty style doc for function print_python_bytes goes there */
/**
 * print_python_bytes - Entry point
 *
 * @p: first arg
 * Return: void
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
    for (i = 0; i < size && i < 10; i++)
        printf("%02hhx%c", str[i], i == 9 ? '\n' : ' ');
}

/* betty style doc for function print_python_float goes there */
/**
 * print_python_float - Entry point
 *
 * @p: first arg
 * Return: void
 */
void print_python_float(PyObject *p) {
    double value;

    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);

    printf("[.] float object info\n");
    printf("  value: %.16g\n", value);
}
