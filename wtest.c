//wtest.c

#include "wtest.h"

void empty_func()
{

}

int simple_func(const char * val)
{
    (void)val;
    return 0;
}

int many_params(int val1, float val2, double val3, const char * val4, const char * val5)
{
    (void)val1;
    (void)val2;
    (void)val3;
    (void)val4;
    (void)val5;
    return 0;
}

int struct_param(Data * val)
{
    (void)val;
    return 0;
}

Data::Data(int v1, int v2, int v3, int v4, float v5, double v6, char * v7)
{
    field1 = v1;
    field2 = v2;
    field3 = v3;
    field4 = v4;
    field5 = v5;
    field6 = v6;
    field7 = v7;
}

Data::Data()
{
    field1 = 0;
    field2 = 0;
    field3 = 0;
    field4 = 0;
    field5 = 0.0;
    field6 = 0.0;
    field7 = 0;
}
