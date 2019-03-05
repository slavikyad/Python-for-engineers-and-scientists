int fac(int n) // ���������� �������, ������� ��������
{
    if (n < 2) return(1);
    return (n)*fac(n-1);
}

#include "Python.h" // �䒺����� ���� Python.h
// ������� ������� �ᒺ�� Python ���� int
static PyObject *Extest_fac(PyObject *self, PyObject *args)
{
    int num;
    // �������� ���� Python ���� int � C++ ���� int
    if (!PyArg_ParseTuple(args, "i", &num)) 
        return NULL;
    // �������� ���� C++ ���� int � Python ���� int
    return (PyObject*)Py_BuildValue("i", fac(num));
}

// ����� ������, �� �������� ������
static PyMethodDef ExtestMethods[] =
{{ "fac", Extest_fac, METH_VARARGS }, { NULL, NULL },};

void initExtest() // ������� ����������� ������
{
    Py_InitModule("Extest", ExtestMethods);
}
