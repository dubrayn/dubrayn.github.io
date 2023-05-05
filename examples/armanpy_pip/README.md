# Python + SWIG test package for PyPi

This simple example shows the correct(?) way to generate and upload a Python + SWIG package to PyPi.

# Compiling and uploading

```bash
$ docker run -it --volume $(pwd):/root/ quay.io/pypa/manylinux_2_28_x86_64
[docker] cd root/
[docker] yum -y install epel-release
[docker] yum -y update
[docker] yum -y install swig armadillo-devel boost-devel
[docker] /opt/python/cp310-cp310/bin/pip3.10 install wheel setuptools numpy twine
[docker] /opt/python/cp310-cp310/bin/pip3.10 wheel . --no-deps -w output
[docker] auditwheel repair output/armanpypsa-*-linux_x86_64.whl -w output
[docker] /opt/python/cp310-cp310/bin/twine upload output/armanpypsa-*-manylinux_2_28_x86_64.whl -r testpypi
```

or simply

```bash
$ docker run -it --volume $(pwd):/root/ quay.io/pypa/manylinux_2_28_x86_64
[docker] cd root/
[docker] ./go.sh
```

## Testing

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ armanpypsa
$ test_package/test.py
```

