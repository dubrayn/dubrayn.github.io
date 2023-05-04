#!/bin/bash

yum -y install epel-release
yum -y update
yum -y install swig armadillo-devel boost-devel
/opt/python/cp310-cp310/bin/pip3.10 install wheel setuptools numpy twine
/opt/python/cp310-cp310/bin/pip3.10 wheel . --no-deps -w output
auditwheel repair output/armanpypsa-*-linux_x86_64.whl -w output
/opt/python/cp310-cp310/bin/twine upload output/armanpypsa-*-manylinux_2_28_x86_64.whl -r testpypi
