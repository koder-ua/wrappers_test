// wtest.i

%module wtest
%{
#include "wtest.h"
%}

struct Data
{
    int field1;
    int field2;
    int field3;
    int field4;

    float field5;
    double field6;
    char * field7;

    Data();
};


void empty_func();
int simple_func(const char * val);
int many_params(int val1, float val2, double val3, const char * val4, const char * val5);
int struct_param(Data * val);
