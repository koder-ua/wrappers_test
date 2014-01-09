import sys

def empty_func():
    pass

def simple_func(val):
    pass

def many_params(val1, val2, val3, val4, val5):
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

def struct_param(val):
    pass

def get_module():
    return sys.modules[__name__]
    