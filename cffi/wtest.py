from cffi import FFI

class Module(object):
    pass

def get_module():
    ffi = FFI()
    ffi.cdef("""
        struct Data
        {
            int field1;
            int field2;
            int field3;
            int field4;

            float field5;
            double field6;
            char * field7;
        };

        void empty_func();
        int simple_func(const char * val);
        int many_params(int val1, float val2, double val3, const char * val4, const char * val5);
        int struct_param(struct Data * val);
    """)


    dll = ffi.dlopen("cffi/_wtest.so")
    mod = Module()

    class Data(object):
        _ffi = ffi
        
        def set_field7(self, val):
            if isinstance(val, str):
                self.field7 = self._ffi.new("char[]", val)
            else:
                self.field7 = val

        def get_field7(self):
            return self._ffi.string(self.field7)
        field7 = property(get_field7, set_field7)

        def __init__(self, field1, field2, field3, field4, field5, field6, field7):
            self.field1 = field1
            self.field2 = field2
            self.field3 = field3
            self.field4 = field4
            self.field5 = field5
            self.field6 = field6
            self.field7 = field7

        def __new__(cls, *dt):
            return cls._ffi.new("struct Data *")

    mod.Data = Data
    mod.empty_func = dll.empty_func
    mod.simple_func = dll.simple_func
    mod.many_params = dll.many_params
    mod.struct_param = dll.struct_param
    return mod

