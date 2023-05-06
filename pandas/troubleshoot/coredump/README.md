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
  (py3.10) $ pip list | grep pandas
  pandas                        1.5.1
  ```
