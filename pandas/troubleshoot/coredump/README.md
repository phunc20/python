- Met coredump on my laptop (Intel(R) Core(TM)2 Duo CPU     L7500  @ 1.60GHz) when
  importing `pandas`
  ```sh
  (py3.10) $ ipython
  import Python 3.10.0 (default, Mar  3 2022, 09:58:08) [GCC 7.5.0]
  Type 'copyright', 'credits' or 'license' for more information
  IPython 8.6.0 -- An enhanced Interactive Python. Type '?' for help.
  
  In [1]: import pandas as pd
  Illegal instruction (core dumped)
  (py3.10) $ coredumpctl
  Sat 2023-05-06 22:35:24 +07 6259 1000 998 SIGILL  present  /home/phunc20/.config/miniconda3/envs/py3.10/bin/python3.10 10.1M
  ```
  One workaround for this is to install Pandas by way of Conda. More precisely,
  the following seems to work.
  ```bash
  $ # This might take longer than simply installing a python environment
  $ conda create -c conda-forge -n vina2vi python=3.10 pandas=2.1.0 tensorflow=2.13.0
  ```
    - <https://tech.amikelive.com/node-887/how-to-resolve-error-illegal-instruction-core-dumped-when-running-import-tensorflow-in-a-python-program/>
