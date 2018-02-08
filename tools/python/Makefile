all: install main calc.so matrix_multiply.so

libtestclass.so: testclass.o
	g++ -shared -fPIC -o $@ $^

main: main.o testclass.o
	g++ -o $@ $^ -larmadillo

%.o: %.cpp
	g++ -std=c++11 -O3 -DARMA_NO_DEBUG -c -o $@ $< -fPIC

build_ext: libtestclass.so
	python setup.py build_ext --swig=${SWIG}

install: build_ext
	python setup.py install --user

matrix_multiply.so: matrix_multiply.py
	pythran $^

calc.so: calc.pyx
	python setup_cython.py build_ext --inplace

clean:
	python setup.py clean
	rm -f testclass.o
	rm -f main.o
	rm -f main
	rm -f matrix_multiply.so
	rm -f libtestclass.a
	rm -f libtestclass.so
	rm -f testclass.py
	rm -f testclass_wrap.cpp
	rm -rf build
	rm -f calc.so
	rm -f calc.c
	find . -name '*.pyc' -delete


