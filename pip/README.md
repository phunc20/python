```bash
# install packages from a text file
pip install -r requirements.txt
# create reproducible package info into a text file
pip freeze > requirements.txt
# install a package in a way that reflect instantaneously the change
pip install -e path/to/some/local/package/
# To check avaiable package versions, e.g. tensorflow
pip install tensorflow==
# `pip search tensorflow` is no longer available
```

