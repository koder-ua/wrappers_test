%Module(name=_wtest, language="C")

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
int simple_func(char * val);
int many_params(int val1, float val2, double val3, char * val4, char * val5);
int struct_param(Data * val);
