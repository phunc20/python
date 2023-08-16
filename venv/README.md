## What Is `venv`?
`venv` is a built-in module for creating
light-weight virtual environment since Python3.5.


## How to Use?
The most frequent use case of `venv` is
```shell
$ python -m venv path/to/your/venv/folder
```

This will, among others,
- Create a virtual environment saved in the above folder
- Create the intermediate folders if they have not already existed
- Put a `bin/` subfolder inside `path/to/your/venv/folder/`, with which
  under Linux you could activate the created virtual environment by
  ```shell
  $ source path/to/your/venv/folder/bin/activate
  (folder) $ 
  ```
  Note that the basename of the folder to which you create the `venv`
  will be your `venv` name
- To deactivate from the virtual environment, just
  ```shell
  (folder) $ deactivate
  $ 
  ```
- The Python version of the created virtual environment will be
  exactly the same as the outer Python which is used to run `python -m venv`.
  For example,
  ```shell
  ~/corbeille/aug15 $ python -m venv a/b/c
  ~/corbeille/aug15 $ ls
  a
  ~/corbeille/aug15 $ source a/b/c/bin/activate
  (c) ~/corbeille/aug15 $ python --version
  Python 3.11.3
  (c) ~/corbeille/aug15 $ deactivate
  ~/corbeille/aug15 $ condact py3.6
  (py3.6) ~/corbeille/aug15 $ python -m venv x/y/z
  (py3.6) ~/corbeille/aug15 $ source x/y/z/bin/activate
  (z) (py3.6) ~/corbeille/aug15 $ which python
  /home/phunc20/corbeille/aug15/x/y/z/bin/python
  (z) (py3.6) ~/corbeille/aug15 $ python --version
  Python 3.6.12 :: Anaconda, Inc.
  (z) (py3.6) ~/corbeille/aug15 $ which pip
  /home/phunc20/corbeille/aug15/x/y/z/bin/pip
  ```

The usual use case is to create a virtual environment using the system's
Python. However, although seemingly redundant, you could also create a
`venv` virtual environment using conda's Python, which may be useful
for OSes like Arch Linux where the system Python may get upgraded as time
goes by (due to rolling release).
