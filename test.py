import sys
import timeit

sys.path.append(sys.argv[1])

stmt = """
import wtest
mod = wtest.get_module()
func = mod.{}
try:
    data = mod.Data(1, 1, 1, 1, 1.0, 1.0, "")
except:
    # for swig
    data = mod.Data()
    data.field1 = 1
    data.field2 = 1
    data.field3 = 1
    data.field4 = 1
    data.field5 = 1.0
    data.field6 = 1.0
    data.field7 = ""
"""

def tt(exec_stmt, setup_stmt, require_time=1):
    res = 0
    num_stmt = 1
    exec_stmt = ";".join([exec_stmt] * num_stmt)
    number = 1
    while res < require_time / 10.0:
        res = timeit.timeit(exec_stmt, setup_stmt, number=number)
        number *= 2

    number = int(number * float(require_time) / res)
    return timeit.timeit(exec_stmt, setup_stmt, number=number) / number / num_stmt

def num_to_user(num):
    coefs = [(1e-9, 'ns'),
             (1e-6, 'us'),
             (1e-3, 'ms')]
    
    for coef, nm in coefs:
        if num / coef < 1:
            return "{:.3f} {}".format(num / coef, nm)
        elif num / coef < 10:
            return "{:1.2f} {}".format(num / coef, nm)
        elif num / coef < 100:
            return "{:2.1f} {}".format(num / coef, nm)
        elif num / coef < 1000:
            return "{}  {}".format(int(num / coef), nm)

    return "{} s".format(num)

print sys.argv[1], ":"
print "    empty  :", num_to_user(tt("func()", stmt.format("empty_func")))
print "    simple :", num_to_user(tt("func('')", stmt.format("simple_func")))
print "    many   :", num_to_user(tt("func(1, 1.0, 1.0, '', '')", stmt.format("many_params")))
print "    struct :", num_to_user(tt("func(data)", stmt.format("struct_param")))
