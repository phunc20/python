## Q&A
1. How to install R language in miniconda?
    - How to know which channel(s) contain(s) R?
        - `conda search <package>`, where `<package>` could be, say,
          `r` or `r-essentials` or `r-recommended` or `r-irkernel`, etc.
        - If you want to know the dependencies, add `--info` to the search command,
          e.g.
          ```shell
          $ conda search r --info
          ...

          r 3.6.0 r36_0
          -------------
          file name   : r-3.6.0-r36_0.conda
          name        : r
          version     : 3.6.0
          build       : r36_0
          build number: 0
          size        : 3 KB
          license     : GPL-3.0
          subdir      : linux-64
          url         : https://repo.anaconda.com/pkgs/r/linux-64/r-3.6.0-r36_0.conda
          md5         : b4ea662a69d5c2aaf304e4c80cb5da9f
          timestamp   : 2019-05-23 07:24:49 UTC
          dependencies:
            - r-base >=3.6,<3.7.0a0
            - r-recommended 3.6.0.*
            - _r-mutex 1.* anacondar_1

          $ 
          ```
1. How to use R language in Jupyter Lab/Notebook?
    - First we need to install `r-irkernel`. Using `$ conda search r-irkernel`
      reveals that, for me on 2023/07/21, the channel `pkgs/r` contains it, so
      ```shell
      $ conda install r-irkernel -c pkgs/r
      ```
    - Next, make sure `jupyter` or `jupyterlab` executable in callable in some
      terminal environment. For example, I have a python enviroment where I have
      previously install `jupyterlab` named `py3.10`, then I could
      ```shell
      $ conda activate py3.10
      $ R
      > IRkernel::installspec()
      >
      ```
        - Failing to have `jupyter` or `jupyterlab` executables available, the
          R command `IRkernel::installspec()` will give an error like the following
          one:
          ```shell
          $ R
          > IRkernel::installspec()
          Error in IRkernel::installspec() :
            jupyter-client has to be installed but “jupyter kernelspec --version” exited with code 1.
          >
          ```
    - Finally, it suffices to open up the `jupyter` or `jupyterlab` of your choice
      (i.e. in which you have installed a R kernel), open a new notebook by
      choosing the kernel to be R and you're good to go


