from ctypes import c_int, c_char_p, CDLL, c_float, byref
from ctypes import c_wchar_p, c_double, Structure, POINTER

class Module(object):
    pass

class Data(Structure):
    _fields_ = [
        ('field1', c_int),
        ('field2', c_int),
        ('field3', c_int),
        ('field4', c_int),
        ('field5', c_float),
        ('field6', c_double),
        ('field7', c_char_p),
    ]

def get_module():
    mod = Module()
    dll = CDLL("ctypes/_wtest.so")

    mod.empty_func = dll.empty_func
    mod.empty_func.arg_types = []
    mod.empty_func.res_type = None
    
    mod.simple_func = dll.simple_func
    mod.simple_func.arg_types = [c_char_p]
    mod.simple_func.res_type = c_int

    _many_params = dll.many_params
    _many_params.arg_types = [c_int, c_float, c_double, c_char_p, c_char_p]
    _many_params.res_type = c_int

    def many_params(val1, val2, val3, val4, val5):
        return _many_params(val1, c_float(val2), c_double(val3), val4, val5)

    mod.many_params = many_params

    _struct_param = dll.struct_param
    _struct_param.arg_types = [POINTER(Data)]
    _struct_param.res_type = c_int

    def struct_param(val):
        return _struct_param(byref(val))

    mod.struct_param = struct_param
    mod.Data = Data
    return mod
