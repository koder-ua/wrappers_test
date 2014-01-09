.PHONY: all clean rebuild test swig ctypes cython cfii boost sip
SHELL=/bin/bash

SWIG_SO=swig/_wtest.so
CTYPES_SO=ctypes/_wtest.so
CYTHON_SO=cython/_wtest.so
CFFI_SO=cffi/_wtest.so
BOOST_SO=boost_python/_wtest.so
SIP_SO=sip/_wtest.so

ALL=$(CTYPES_SO) $(SWIG_SO) $(CYTHON_SO) $(CFFI_SO) $(BOOST_SO) $(SIP_SO)
LIB_C_FILE=wtest.c
LIB_CODE=wtest.h $(LIB_C_FILE)


all: $(ALL)

swog: $(SWIG_SO)
$(SWIG_SO): $(LIB_CODE) swig/wtest.i
		swig -python -o swig/wtest.cpp swig/wtest.i
		g++ -shared -fpic -o $(SWIG_SO) swig/wtest.cpp $(LIB_C_FILE) -I . -I /usr/include/python2.7
		echo "import sys" >> swig/wtest.py
		echo "def get_module():" >> swig/wtest.py
		echo "    return sys.modules[__name__]" >> swig/wtest.py

ctypes: $(CTYPES_SO)
$(CTYPES_SO): $(LIB_CODE)
		g++ -shared -fpic -o $(CTYPES_SO) $(LIB_C_FILE) -I . -I /usr/include/python2.7

cython: $(CYTHON_SO)
$(CYTHON_SO): $(LIB_CODE) cython/_wtest.pyx
		cython -o cython/_wtest.c cython/_wtest.pyx
		g++ -shared -fpic -o $(CYTHON_SO) cython/_wtest.c $(LIB_C_FILE) -I . -I /usr/include/python2.7

cffi: $(CFFI_SO)
$(CFFI_SO): $(LIB_CODE)
		g++ -shared -fpic -o $(CFFI_SO) $(LIB_C_FILE) -I . -I /usr/include/python2.7

boost: $(BOOST_SO)
$(BOOST_SO): $(LIB_CODE) boost_python/wtest.c
		g++ -shared -fpic -o $(BOOST_SO) $(LIB_C_FILE) boost_python/wtest.c -I . -I /usr/include/python2.7 -l boost_python-py27

sip: $(SIP_SO)
$(SIP_SO): $(LIB_CODE) sip/wtest.sip
		sip -c sip -b sip/wtest.sbf sip/wtest.sip
		sed -i '1i#include "wtest.h"' sip/sip_wtestcmodule.c
		g++ sip/sip_wtestcmodule.c $(LIB_C_FILE) -I . -I /usr/include/python2.7 -fpic -shared -o sip/_wtest.so

clean:
	-rm $(ALL)

rebuild: clean all

TIMEIT=python test.py

DIRS=ppython cython ctypes cffi swig boost_python sip
DIRS=ppython cython ctypes cffi swig boost_python

test: $(ALL)
		$(foreach var,$(DIRS),$(TIMEIT) $(var);)



