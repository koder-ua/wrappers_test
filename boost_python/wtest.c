#include <boost/python/def.hpp>
#include <boost/python/class.hpp>
#include <boost/python/module.hpp>

#include "wtest.h"

BOOST_PYTHON_MODULE(_wtest)
{
    using namespace boost::python;

    def("empty_func", empty_func);
    def("simple_func", simple_func);
    def("many_params", many_params);
    def("struct_param", struct_param);

    class_<Data>("Data")
        .def_readwrite("field1", &Data::field1)
        .def_readwrite("field3", &Data::field2)
        .def_readwrite("field3", &Data::field3)
        .def_readwrite("field4", &Data::field4)
        .def_readwrite("field5", &Data::field5)
        .def_readwrite("field6", &Data::field6)
        .def_readwrite("field7", &Data::field7);
}
