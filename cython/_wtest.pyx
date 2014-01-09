cdef extern from "wtest.h":

    cdef struct Data:
        int field1
        int field2
        int field3
        int field4
        float field5
        double field6
        char * field7
        

    void empty_func()
    int simple_func(char * val)
    int many_params(int val1, float val2, double val3, char * val4, char * val5)
    int struct_param(Data * val)


def py_empty_func():
    empty_func()

def py_simple_func(val):
    return simple_func(val)

def py_many_params(val1, val2, val3, val4, val5):
    return many_params(val1, val2, val3, val4, val5)

def py_struct_param(val):
    cdef Data data

    data.field1 = val.field1
    data.field2 = val.field2
    data.field3 = val.field3
    data.field4 = val.field4
    data.field5 = val.field5
    data.field6 = val.field6
    data.field7 = val.field7
    
    return struct_param(&data)

