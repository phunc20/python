## By default, one cannot `plt.show()` to show plots/images
- In `miniconda` on Arch Linux, the following works -- namely, declar by **`matplotlib.use("TkAgg")`**
  ```bash
  (tf2) ~/.../2019/01-neural-networks-deep-learning/03_shallow-neural-networks ❯❯❯ condactivate tf2
  (tf2) ~/.../2019/01-neural-networks-deep-learning/03_shallow-neural-networks ❯❯❯ ipython
  Python 3.8.5 (default, Sep  4 2020, 07:30:14)
  Type 'copyright', 'credits' or 'license' for more information
  IPython 7.19.0 -- An enhanced Interactive Python. Type '?' for help.
  
  In [1]: import tkinter
  
  In [2]: import matplotlib
  
  In [3]: matplotlib.use("agg")
  
  In [4]: import matplotlib.pyplot as plt
  
  In [5]: plt.scatter([1,2,3,4], [-1,-2,-3,100])
  Out[5]: <matplotlib.collections.PathCollection at 0x7fcfc8d3cbe0>
  
  In [6]: plt.show()
  <ipython-input-6-1eb00ff78cf2>:1: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  plt.show()
  
  In [7]: matplotlib.use("t")
  ---------------------------------------------------------------------------
  ValueError                                Traceback (most recent call last)
  <ipython-input-7-983d480f2ff2> in <module>
  ----> 1 matplotlib.use("t")
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/matplotlib/__init__.py in use(backend, force)
     1143     matplotlib.get_backend
     1144     """
  -> 1145     name = validate_backend(backend)
     1146     # we need to use the base-class method here to avoid (prematurely)
     1147     # resolving the "auto" backend setting
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/matplotlib/rcsetup.py in validate_backend(s)
      293     backend = (
      294         s if s is _auto_backend_sentinel or s.startswith("module://")
  --> 295         else _validate_standard_backends(s))
      296     return backend
      297
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/matplotlib/rcsetup.py in __call__(self, s)
       79                 and s[1:-1] in self.valid):
       80             msg += "; remove quotes surrounding your string"
  ---> 81         raise ValueError(msg)
       82
       83
  
  ValueError: 't' is not a valid value for backend; supported values are ['GTK3Agg', 'GTK3Cairo', 'MacOSX', 'nbAgg', 'Qt4Agg', 'Qt4Cairo', 'Qt5Agg', 'Qt5Cairo', 'TkAgg', 'TkCairo', 'WebAgg', 'WX', 'WXAgg', 'WXCairo', 'agg', 'cairo', 'pdf', 'pgf', 'ps', 'svg', 'template']
  
  In [8]: matplotlib.use("TkAgg")
  
  In [9]: plt.show()
  
  In [10]: plt.scatter([1,2,3,4], [-1,-2,-3,100])
  Out[10]: <matplotlib.collections.PathCollection at 0x7fcfb2c58640>
  
  In [11]: plt.show()
  
  In [12]:
  ```
  - Note that if you accidentally typed sth inexistent, say like above `matplotlib.use("t")`, `matplotlib` will remind you of the supported values: `['GTK3Agg', 'GTK3Cairo', 'MacOSX', 'nbAgg', 'Qt4Agg', 'Qt4Cairo', 'Qt5Agg', 'Qt5Cairo', 'TkAgg', 'TkCairo', 'WebAgg', 'WX', 'WXAgg', 'WXCairo', 'agg', 'cairo', 'pdf', 'pgf', 'ps', 'svg', 'template']`


## Misc
- Demo: using `cairo` in `matplotlib.use()`
  ```ipython
  In [12]: matplotlib.use("cairo")
  ---------------------------------------------------------------------------
  ModuleNotFoundError                       Traceback (most recent call last)
  ~/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/matplotlib/backends/backend_cairo.py in <module>
       14 try:
  ---> 15     import cairo
       16     if cairo.version_info < (1, 11, 0):
  
  ModuleNotFoundError: No module named 'cairo'
  
  During handling of the above exception, another exception occurred:
  
  ModuleNotFoundError                       Traceback (most recent call last)
  ~/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/matplotlib/backends/backend_cairo.py in <module>
       20     try:
  ---> 21         import cairocffi as cairo
       22     except ImportError as err:
  
  ModuleNotFoundError: No module named 'cairocffi'
  
  The above exception was the direct cause of the following exception:
  
  ImportError                               Traceback (most recent call last)
  <ipython-input-12-3a3e2d3e4056> in <module>
  ----> 1 matplotlib.use("cairo")
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/matplotlib/__init__.py in use(backend, force)
     1160                 # user does not have the libraries to support their
     1161                 # chosen backend installed.
  -> 1162                 plt.switch_backend(name)
     1163             except ImportError:
     1164                 if force:
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/matplotlib/pyplot.py in switch_backend(newbackend)
      274     backend_name = cbook._backend_module_name(newbackend)
      275
  --> 276     class backend_mod(matplotlib.backend_bases._Backend):
      277         locals().update(vars(importlib.import_module(backend_name)))
      278
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/matplotlib/pyplot.py in backend_mod()
      275
      276     class backend_mod(matplotlib.backend_bases._Backend):
  --> 277         locals().update(vars(importlib.import_module(backend_name)))
      278
      279     required_framework = _get_required_interactive_framework(backend_mod)
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/importlib/__init__.py in import_module(name, package)
      125                 break
      126             level += 1
  --> 127     return _bootstrap._gcd_import(name[level:], package, level)
      128
      129
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/importlib/_bootstrap.py in _gcd_import(name, package, level)
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/importlib/_bootstrap.py in _find_and_load(name, import_)
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/importlib/_bootstrap.py in _find_and_load_unlocked(name, import_)
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/importlib/_bootstrap.py in _load_unlocked(spec)
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/importlib/_bootstrap_external.py in exec_module(self, module)
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/importlib/_bootstrap.py in _call_with_frames_removed(f, *args, **kwds)
  
  ~/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/matplotlib/backends/backend_cairo.py in <module>
       21         import cairocffi as cairo
       22     except ImportError as err:
  ---> 23         raise ImportError(
       24             "cairo backend requires that pycairo>=1.11.0 or cairocffi"
       25             "is installed") from err
  
  ImportError: cairo backend requires that pycairo>=1.11.0 or cairocffiis installed
  
  In [13]: !pip search pycairo
  ERROR: Exception:
  Traceback (most recent call last):
  File "/home/phunc20/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/pip/_internal/cli/base_command.py", line 228, in _main
        status = self.run(options, args)
  File "/home/phunc20/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/pip/_internal/commands/search.py", line 60, in run
        pypi_hits = self.search(query, options)
  File "/home/phunc20/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/pip/_internal/commands/search.py", line 80, in search
        hits = pypi.search({'name': query, 'summary': query}, 'or')
          File "/home/phunc20/.config/miniconda3/envs/tf2/lib/python3.8/xmlrpc/client.py", line 1109, in __call__
      return self.__send(self.__name, args)
        File "/home/phunc20/.config/miniconda3/envs/tf2/lib/python3.8/xmlrpc/client.py", line 1450, in __request
            response = self.__transport.request(
      File "/home/phunc20/.config/miniconda3/envs/tf2/lib/python3.8/site-packages/pip/_internal/network/xmlrpc.py", line 45, in request
          return self.parse_response(response.raw)
    File "/home/phunc20/.config/miniconda3/envs/tf2/lib/python3.8/xmlrpc/client.py", line 1341, in parse_response
        return u.close()
          File "/home/phunc20/.config/miniconda3/envs/tf2/lib/python3.8/xmlrpc/client.py", line 655, in close
      raise Fault(**self._stack[0])
      xmlrpc.client.Fault: <Fault -32500: "RuntimeError: PyPI's XMLRPC API has been temporarily disabled due to unmanageable load and will be deprecated in the near future. See https://status.python.org/ for more information.">
  
  In [14]: !conda list | grep cairo
  
  In [15]: !conda list | grep tensor
  tensorboard               2.3.0              pyh4dce500_0
  tensorboard-plugin-wit    1.6.0                      py_0
  tensorflow                2.3.0           eigen_py38h71ff20e_0
  tensorflow-base           2.3.0           eigen_py38hb57a387_0
  tensorflow-estimator      2.3.0              pyheb71bc4_0
  
  In [16]: !conda search cairo
  Loading channels: done
  # Name                       Version           Build  Channel
  cairo                        1.14.10      h58b644b_4  pkgs/main
  cairo                        1.14.10      haa5651f_5  pkgs/main
  cairo                        1.14.10      hdf128ce_6  pkgs/main
  cairo                        1.14.12      h7636065_2  pkgs/main
  cairo                        1.14.12      h77bcde2_0  pkgs/main
  cairo                        1.14.12      h8948797_3  pkgs/main
  
  In [17]: !conda search pycairo
  Loading channels: done
  # Name                       Version           Build  Channel
  pycairo                       1.13.3  py27h44fc0e4_1  pkgs/main
  pycairo                       1.13.3  py27hea6d626_0  pkgs/main
  pycairo                       1.13.3  py35h77ace0a_1  pkgs/main
  pycairo                       1.13.3  py36h8764da6_1  pkgs/main
  pycairo                       1.15.4  py27h1b9232e_1  pkgs/main
  pycairo                       1.15.4  py35h1b9232e_1  pkgs/main
  pycairo                       1.15.4  py36h1b9232e_1  pkgs/main
  pycairo                       1.15.4  py37h1b9232e_1  pkgs/main
  pycairo                       1.17.1  py27h2a1e443_0  pkgs/main
  pycairo                       1.17.1  py35h2a1e443_0  pkgs/main
  pycairo                       1.17.1  py36h2a1e443_0  pkgs/main
  pycairo                       1.17.1  py37h2a1e443_0  pkgs/main
  pycairo                       1.18.0  py27h2a1e443_0  pkgs/main
  pycairo                       1.18.0  py36h2a1e443_0  pkgs/main
  pycairo                       1.18.0  py37h2a1e443_0  pkgs/main
  pycairo                       1.18.1  py27h2a1e443_0  pkgs/main
  pycairo                       1.18.1  py36h2a1e443_0  pkgs/main
  pycairo                       1.18.1  py37h2a1e443_0  pkgs/main
  pycairo                       1.18.2  py27h2a1e443_0  pkgs/main
  pycairo                       1.18.2  py36h2a1e443_0  pkgs/main
  pycairo                       1.18.2  py37h2a1e443_0  pkgs/main
  pycairo                       1.18.2  py38h2a1e443_0  pkgs/main
  pycairo                       1.19.0  py36h2a1e443_0  pkgs/main
  pycairo                       1.19.0  py37h2a1e443_0  pkgs/main
  pycairo                       1.19.0  py38h2a1e443_0  pkgs/main
  pycairo                       1.19.1  py36h2a1e443_0  pkgs/main
  pycairo                       1.19.1  py37h2a1e443_0  pkgs/main
  pycairo                       1.19.1  py38h2a1e443_0  pkgs/main
  
  In [18]: #!conda install -n tf2
  
  In [19]: !which python
  /home/phunc20/.config/miniconda3/envs/tf2/bin/python
  
  In [20]: !conda install -n tf2 pycairo -y
  Collecting package metadata (current_repodata.json): done
  Solving environment: done
  
  
    ==> WARNING: A newer version of conda exists. <==
  current version: 4.8.3
    latest version: 4.9.2
  
  Please update conda by running
  
    $ conda update -n base -c defaults conda
  
  
  
    ## Package Plan ##
  
  environment location: /home/phunc20/.config/miniconda3/envs/tf2
  
    added / updated specs:
    - pycairo
  
  
    The following packages will be downloaded:
  
    package                    |            build
    ---------------------------|-----------------
    cairo-1.14.12              |       h8948797_3         906 KB
    pixman-0.40.0              |       h7b6447c_0         370 KB
    pycairo-1.19.1             |   py38h2a1e443_0          74 KB
    ------------------------------------------------------------
                                           Total:         1.3 MB
  
   The following NEW packages will be INSTALLED:
  
     cairo              pkgs/main/linux-64::cairo-1.14.12-h8948797_3
   pixman             pkgs/main/linux-64::pixman-0.40.0-h7b6447c_0
     pycairo            pkgs/main/linux-64::pycairo-1.19.1-py38h2a1e443_0
  
  
  
     Downloading and Extracting Packages
     cairo-1.14.12        | 906 KB    | ######################################################################## | 100%
     pycairo-1.19.1       | 74 KB     | ######################################################################## | 100%
     pixman-0.40.0        | 370 KB    | ######################################################################## | 100%
     Preparing transaction: done
     Verifying transaction: done
     Executing transaction: done
  
  In [21]: matplotlib.use("cairo")
  
  In [22]: plt.scatter([1,2,3,4], [-1,-2,-3,100])
  Out[22]: <matplotlib.collections.PathCollection at 0x7fcfb2360130>
  
  In [23]: plt.show()
  <ipython-input-23-1eb00ff78cf2>:1: UserWarning: Matplotlib is currently using cairo, which is a non-GUI backend, so cannot show the figure.
   plt.show()
  
  In [24]:
  ```
