import _wtest

class Module(object):
    pass

class Data(object):
    def __init__(self, field1, field2, field3, field4, field5, field6, field7):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.field4 = field4
        self.field5 = field5
        self.field6 = field6
        self.field7 = field7

def get_module():
    mod = Module()
    mod.empty_func = _wtest.py_empty_func
    mod.simple_func = _wtest.py_simple_func
    mod.many_params = _wtest.py_many_params
    mod.struct_param = _wtest.py_struct_param
    mod.Data = Data
    return mod
