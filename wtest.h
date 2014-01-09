// wtest.h
#ifndef WTEST_H_
#define WTEST_H_

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
    Data(int v1, int v2, int v3, int v4, float v5, double v6, char * v7);
};

extern "C"
{

    void empty_func();
    int simple_func(const char * val);
    int many_params(int val1, float val2, double val3, const char * val4, const char * val5);
    int struct_param(Data * val);
}

#endif //!WTEST_H_
