# Python + SWIG test package

This simple example shows the correct(?) way to generate and deploy a Python + SWIG package.

# Installation in a venv

Create a `venv` and activate it.

```shell
python3 -m venv venv
source venv/bin/activate
```

Then generate the package and deploy it.

```shell
python3 -m pip install .
```

You can finally test the package.

```shell
cd test_package
python3 test.py
```


