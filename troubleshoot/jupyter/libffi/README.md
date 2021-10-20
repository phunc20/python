## Problem Description
On my Arch Linux (Thinkpad X201), after `pacman -Syu`, suddenly I cannot run `jupyter notebook` any more.
My virtualenv uses Python3.7 that I manually installed from the official website.

```
(oft) ~ ❯❯❯ ju
Traceback (most recent call last):
  File "/home/phunc20/.virtualenvs/oft/bin/jupyter-notebook", line 5, in <module>
    from notebook.notebookapp import main
  File "/home/phunc20/.virtualenvs/oft/lib/python3.7/site-packages/notebook/notebookapp.py", line 76, in <module>
    from .base.handlers import Template404, RedirectWithParams
  File "/home/phunc20/.virtualenvs/oft/lib/python3.7/site-packages/notebook/base/handlers.py", line 35, in <module>
    from notebook.utils import is_hidden, url_path_join, url_is_absolute, url_escape, urldecode_unix_socket_path
  File "/home/phunc20/.virtualenvs/oft/lib/python3.7/site-packages/notebook/utils.py", line 8, in <module>
    import ctypes
  File "/usr/local/lib/python3.7/ctypes/__init__.py", line 7, in <module>
    from _ctypes import Union, Structure, Array
ImportError: libffi.so.7: cannot open shared object file: No such file or directory
(oft) ~ ❯❯❯ sudo find /usr/lib -name "libffi*"
/usr/lib/libffi.so
/usr/lib/libffi.so.8
/usr/lib/pkgconfig/libffi.pc
/usr/lib/libffi.so.8.1.0
```

- Possible solution: Reinstall Python, so that it knows that the system has updated `libffi` to version 8.
- Alternative: On Arch Linux, there is system-installed Python (usually its version will be really new, because Arch is rolling distro). Use that Python and it's almost sure that it is aware of the latest library changes.
