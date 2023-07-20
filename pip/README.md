```shell
# Help messages, e.g.
pip --help
man pip
pip install --help

# install packages from a text file
pip install -r requirements.txt
# create reproducible package info into a text file
pip freeze > requirements.txt

# install a package in a way that reflect instantaneously the change
pip install -e path/to/some/local/package/

# To check avaiable package versions, e.g. tensorflow
pip install tensorflow==
# `pip search tensorflow` is no longer available

# To give less output (stdout)
pip install -q <some_package(s)>
# Could request the utmost quietness with three consecutive Q's
pip install -qqq <some_package(s)>
```


## Install A Local Package
That is, install a Python package from files local to your machine.
There seem to exist at least two ways

1. `pip install -e <path>`, where `<path>` is a folder possessing a `setup.py` file
  - The `-e` option means **"editable"**, i.e. when you edit the Python code inside `<path>`, your program using that package will reflect the changes immediately.
1. `python setup.py install` when you are inside `<path>`, where `<path>` is as described above.
