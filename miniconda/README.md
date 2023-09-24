## Installation
1. Go download the installation shell script from <https://docs.conda.io/en/latest/miniconda.html> suitable for your OS
1. Check its sha256sum, say, by `diff <(echo <the_provided_sum>) <(sha256sum <downloaded_miniconda.sh> | awk '{ print $1 }')`
1. Install by running `sh <downloaded_miniconda.sh>`


## Troubleshoot
- Cannot install a virtual environment with older versions of Python (e.g. Python3.3)?
    - You might not look into the right channel: (The default channel being `pkgs/main`)
      ```bash
      $ conda search python -c pkgs/main | grep "^python\s*3.4"
      $ conda search python -c conda-forge | grep "^python\s*3.4"
      python                         3.4.5               0  conda-forge
      python                         3.4.5               1  conda-forge
      python                         3.4.5               2  conda-forge
      $ conda search python -c free | grep "^python\s*3.[3-4]"
      python                         3.3.0               2  free
      python                         3.3.0               3  free
      python                         3.3.0               4  free
      python                         3.3.1               0  free
      python                         3.3.2               0  free
      python                         3.3.2               1  free
      python                         3.3.3               0  free
      python                         3.3.4               0  free
      python                         3.3.5               0  free
      python                         3.3.5               1  free
      python                         3.3.5               2  free
      python                         3.3.5               3  free
      python                         3.3.5               4  free
      python                         3.4.0               0  free
      python                         3.4.1               0  free
      python                         3.4.1               1  free
      python                         3.4.1               2  free
      python                         3.4.1               3  free
      python                         3.4.1               4  free
      python                         3.4.2               0  free
      python                         3.4.3               0  free
      python                         3.4.3               1  free
      python                         3.4.3               2  free
      python                         3.4.4               0  free
      python                         3.4.4               5  free
      python                         3.4.5               0  free
      ```
      For example, we have found that the `free` channel contains Python3.3. We could install like this:
      ```bash
      $ conda create -n py3.3 python=3.3 -c free
      ```
- How to specify a package's installed version? Furthermore, when one version has more than one build, how to specify the one you want to install?
  ```bash
  (py3.6) ~ ❯❯❯ conda search tensorflow
  Loading channels: done
  # Name                       Version           Build  Channel
  ...
  tensorflow                     1.6.0               0  pkgs/main
  tensorflow                     1.7.0               0  pkgs/main
  tensorflow                     1.8.0               0  pkgs/main
  tensorflow                     1.8.0      h01c6a4e_0  pkgs/main
  tensorflow                     1.8.0      h16da8f2_0  pkgs/main
  tensorflow                     1.8.0      h2742514_0  pkgs/main
  tensorflow                     1.8.0      h469b60b_0  pkgs/main
  tensorflow                     1.8.0      h57681fa_0  pkgs/main
  tensorflow                     1.8.0      h5c3c37f_0  pkgs/main
  tensorflow                     1.8.0      h645107b_0  pkgs/main
  tensorflow                     1.8.0      h7b2774c_0  pkgs/main
  tensorflow                     1.8.0      hb11d968_0  pkgs/main
  tensorflow                     1.8.0      hb1b1514_0  pkgs/main
  tensorflow                     1.8.0      hb381393_0  pkgs/main
  tensorflow                     1.8.0      hc2d9325_0  pkgs/main
  tensorflow                     1.9.0 eigen_py27hf386fcc_1  pkgs/main
  tensorflow                     1.9.0 eigen_py35h8c89287_1  pkgs/main
  tensorflow                     1.9.0 eigen_py36h8c89287_0  pkgs/main
  tensorflow                     1.9.0 eigen_py36hbec2359_0  pkgs/main
  tensorflow                     1.9.0 eigen_py36hbec2359_1  pkgs/main
  tensorflow                     1.9.0 eigen_py36hf386fcc_0  pkgs/main
  tensorflow                     1.9.0 gpu_py27h233f449_1  pkgs/main
  tensorflow                     1.9.0 gpu_py27h395d940_1  pkgs/main
  tensorflow                     1.9.0 gpu_py27hd3a791e_1  pkgs/main
  tensorflow                     1.9.0 gpu_py35h42d5ad8_1  pkgs/main
  tensorflow                     1.9.0 gpu_py35h60c0932_1  pkgs/main
  tensorflow                     1.9.0 gpu_py35hb39db67_1  pkgs/main
  tensorflow                     1.9.0 gpu_py36h02c5d5e_1  pkgs/main
  tensorflow                     1.9.0 gpu_py36h220e158_1  pkgs/main
  tensorflow                     1.9.0 gpu_py36h313df88_1  pkgs/main
  tensorflow                     1.9.0 mkl_py27h0cb61a4_1  pkgs/main
  tensorflow                     1.9.0 mkl_py35h5be851a_1  pkgs/main
  tensorflow                     1.9.0 mkl_py36h0cb61a4_0  pkgs/main
  tensorflow                     1.9.0 mkl_py36h5be851a_0  pkgs/main
  tensorflow                     1.9.0 mkl_py36h6d6ce78_0  pkgs/main
  tensorflow                     1.9.0 mkl_py36h6d6ce78_1  pkgs/main
  ...
  ~ ❯❯❯ conda search tensorflow-gpu
  Loading channels: done
  # Name                       Version           Build  Channel
  tensorflow-gpu                 1.4.1               0  pkgs/main
  tensorflow-gpu                 1.5.0               0  pkgs/main
  tensorflow-gpu                 1.6.0               0  pkgs/main
  tensorflow-gpu                 1.7.0               0  pkgs/main
  tensorflow-gpu                 1.8.0      h7b35bdc_0  pkgs/main
  tensorflow-gpu                 1.9.0      hf154084_0  pkgs/main
  tensorflow-gpu                1.10.0      hf154084_0  pkgs/main
  tensorflow-gpu                1.11.0      h0d30ee6_0  pkgs/main
  tensorflow-gpu                1.12.0      h0d30ee6_0  pkgs/main
  tensorflow-gpu                1.13.1      h0d30ee6_0  pkgs/main
  tensorflow-gpu                1.14.0      h0d30ee6_0  pkgs/main
  tensorflow-gpu                1.15.0      h0d30ee6_0  pkgs/main
  tensorflow-gpu                 2.0.0      h0d30ee6_0  pkgs/main
  tensorflow-gpu                 2.1.0      h0d30ee6_0  pkgs/main
  tensorflow-gpu                 2.2.0      h0d30ee6_0  pkgs/main
  (py3.6) ~ ❯❯❯
  ```
  - **`conda install -n homl-1e tensorflow-gpu=1.13.1`**


## Cheatsheet
```bash
# remove an env
conda remove --name abc --all
conda env remove --name pDL

# list all existing envs
conda info --envs
# create an env based on the yaml file `environment.yml`
conda env create -f environment.yml

# create an empty env called `sociald`
conda create -n sociald
# As of 2020/12/31, conda3's default python environment is python3.7
# To install an env with python3.6, do as follows
conda create -n py3.6 python=3.6

# search for packages
conda search opencv
# search for available Python versions
conda search --full-name python

# install a package  # Here, assume the env name is "tf2"
conda install -n tf2 jupyterlab
# Use -y in situations where you cannot confirm by typing into stdout, e.g. in a jupyter cell:
conda install -n tf2 matplotlib -y
# install a package with a specific version instead of the latest one
conda install -n tf2 tensorflow-gpu=2.1.0
# More precisely,
conda install -c <channel> -n <env> pandas=<version>=<build>
# install from another channel (the `-c` option), say, from conda-forge
conda install -n tf2 nbdime -c conda-forge


# uninstall a package from a particular env
conda remove -n tf2 matplotlib
# uninstall a package from the current env
conda remove matplotlib

# export your env to share w/ others
conda activate <env_name>
conda env export > environment.yml

# create a new env via an environment.yml file
conda env create -f environment.yml

# remove an env
# either
conda remove --name myenv --all
# or
conda env remove --name myenv

conda config --set auto_activate_base false
conda config --set auto_activate_base true

# list all installed packages under a certain env, e.g. env named `oft`
conda list -n oft
# To check if a certain package is installed under some env
# e.g. check for the jedi package in env "homl1e"
~/.../phunc20/python/miniconda ❯❯❯ conda list -n homl1e | grep jedi
jedi                      0.17.0                   py37_0
```

- **cf.** [https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#removing-an-environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#removing-an-environment)


### Create an virtualenv from a `yml` file
```bash
conda env create -f environment.yml

(pDL) [phunc20@homography-x220t pytorch-Deep-Learning]$ cat environment.yml
name: pDL
channels:
  - conda-forge
  - pytorch
  - dglteam
dependencies:
  - python=3.8
  - pip
  - matplotlib
  - jupyter
  - jupyterlab
  - pytorch>=1.4
  - cpuonly
  - torchvision>=0.5
  - torchtext
  - opencv
  - librosa
  - nb_conda_kernels
  - dgl>=0.4.3
  - pip:
    - torchviz
```


## No `conda` command?
The following works on Fedora:<br>
Reading closely, when you install miniconda, there are guiding messages. For example, I have put my installation in `~/.config/`. Then the next command
enables one to have `conda` command back.
```bash
eval "$(/home/phunc20/.config/miniconda3/bin/conda shell.bash hook)"
```
To permanently possessing the `conda` command, run a further command:
```bash
conda init
```


### `(base)` by default or not
Once you finish installing miniconda, if you choose everything as the default during installation,
the `(base)` environment will be **auto-activated**.

You may not like this default setting. If that's the case, you can always modify that by

```bash
## If you'd prefer that conda's base environment not be activated on startup
conda config --set auto_activate_base false
## And if you'd like to have (base) back
conda config --set auto_activate_base true
```


```bash
[phunc20@homography-x220t pytorch-Deep-Learning]$ conda info --envs
# conda environments:
#
base                  *  /home/phunc20/.config/miniconda3
abc                      /home/phunc20/.config/miniconda3/envs/abc
pDL                      /home/phunc20/.config/miniconda3/envs/pDL

[phunc20@homography-x220t pytorch-Deep-Learning]$ conda remove --name abc

CondaValueError: no package names supplied,
       try "conda remove -h" for more details

[phunc20@homography-x220t pytorch-Deep-Learning]$ conda remove --name abc --all

Remove all packages in environment /home/phunc20/.config/miniconda3/envs/abc:


## Package Plan ##

  environment location: /home/phunc20/.config/miniconda3/envs/abc


The following packages will be REMOVED:

  _libgcc_mutex-0.1-conda_forge
  _openmp_mutex-4.5-1_llvm
  appdirs-1.4.4-pyh9f0ad1d_0
  argon2-cffi-20.1.0-py38h1e0a361_2
  async_generator-1.10-py_0
  attrs-20.3.0-pyhd3deb0d_0
  audioread-2.1.8-py38h32f6830_3
  backcall-0.2.0-pyh9f0ad1d_0
  backports-1.0-py_2
  backports.functools_lru_cache-1.6.1-py_0
  blas-2.20-mkl
  bleach-3.2.1-pyh9f0ad1d_0
  brotlipy-0.7.0-py38h8df0ef7_1001
  bzip2-1.0.8-h516909a_3
  c-ares-1.16.1-h516909a_3
  ca-certificates-2020.11.8-ha878542_0
  cairo-1.16.0-h9f066cc_1006
  certifi-2020.6.20-py38h924ce5b_2
  cffi-1.14.3-py38h1bdcb99_1
  chardet-3.0.4-py38h924ce5b_1008
  cpuonly-1.0-0
  cryptography-3.2.1-py38h7699a38_0
  cycler-0.10.0-py_2
  dbus-1.13.6-hfdff14a_1
  decorator-4.4.2-py_0
  defusedxml-0.6.0-py_0
  dgl-0.5.2-py38_0
  entrypoints-0.3-py38h32f6830_1002
  expat-2.2.9-he1b5a44_2
  ffmpeg-4.3.1-h3215721_1
  fontconfig-2.13.1-h7e3eb15_1002
  freetype-2.10.4-h7ca028e_0
  gettext-0.19.8.1-hf34092f_1004
  glib-2.66.2-h58526e2_0
  gmp-6.2.0-h58526e2_4
  gnutls-3.6.13-h79a8f9a_0
  graphite2-1.3.13-h58526e2_1001
  gst-plugins-base-1.14.5-h0935bb2_2
  gstreamer-1.14.5-h36ae1b5_2
  harfbuzz-2.7.2-hb1ce69c_1
  hdf5-1.10.6-nompi_h54c07f9_1110
  icu-67.1-he1b5a44_0
  idna-2.10-pyh9f0ad1d_0
  importlib-metadata-2.0.0-py_1
  importlib_metadata-2.0.0-1
  ipykernel-5.3.4-py38h1cdfbd6_1
  ipython-7.19.0-py38h81c977d_0
  ipython_genutils-0.2.0-py_1
  ipywidgets-7.5.1-pyh9f0ad1d_1
  jasper-1.900.1-h07fcdf6_1006
  jedi-0.17.2-py38h578d9bd_1
  jinja2-2.11.2-pyh9f0ad1d_0
  joblib-0.17.0-py_0
  jpeg-9d-h36c2ea0_0
  json5-0.9.5-pyh9f0ad1d_0
  jsonschema-3.2.0-py_2
  jupyter-1.0.0-py_2
  jupyter_client-6.1.7-py_0
  jupyter_console-6.2.0-py_0
  jupyter_core-4.6.3-py38h32f6830_2
  jupyterlab-2.2.9-py_0
  jupyterlab_pygments-0.1.2-pyh9f0ad1d_0
  jupyterlab_server-1.2.0-py_0
  kiwisolver-1.3.1-py38h82cb98a_0
  krb5-1.17.1-hfafb76e_3
  lame-3.100-h14c3975_1001
  lcms2-2.11-hcbb858e_1
  ld_impl_linux-64-2.35-h769bd43_9
  libblas-3.8.0-20_mkl
  libcblas-3.8.0-20_mkl
  libclang-10.0.1-default_hde54327_1
  libcurl-7.71.1-hcdd3856_8
  libedit-3.1.20191231-he28a2e2_2
  libev-4.33-h516909a_1
  libevent-2.1.10-hcdb4288_3
  libffi-3.2.1-he1b5a44_1007
  libflac-1.3.3-he1b5a44_0
  libgcc-ng-9.3.0-h5dbcf3e_17
  libgfortran-ng-7.5.0-hae1eefd_17
  libgfortran4-7.5.0-hae1eefd_17
  libglib-2.66.2-hbe7bbb4_0
  libiconv-1.16-h516909a_0
  liblapack-3.8.0-20_mkl
  liblapacke-3.8.0-20_mkl
  libllvm10-10.0.1-he513fc3_3
  libnghttp2-1.41.0-h8cfc5f6_2
  libogg-1.3.2-h516909a_1002
  libopencv-4.5.0-py38_2
  libpng-1.6.37-h21135ba_2
  libpq-12.3-h5513abc_2
  librosa-0.8.0-pyh9f0ad1d_0
  libsndfile-1.0.29-he1b5a44_0
  libsodium-1.0.18-h516909a_1
  libssh2-1.9.0-hab1572f_5
  libstdcxx-ng-9.3.0-h2ae2ef3_17
  libtiff-4.1.0-h4f3a223_6
  libuuid-2.32.1-h14c3975_1000
  libuv-1.40.0-hd18ef5c_0
  libvorbis-1.3.7-he1b5a44_0
  libwebp-base-1.1.0-h36c2ea0_3
  libxcb-1.13-h14c3975_1002
  libxkbcommon-0.10.0-he1b5a44_0
  libxml2-2.9.10-h68273f3_2
  llvm-openmp-11.0.0-hfc4b9b4_1
  llvmlite-0.34.0-py38h4f45e52_2
  lz4-c-1.9.2-he1b5a44_3
  markupsafe-1.1.1-py38h8df0ef7_2
  matplotlib-3.3.2-py38h578d9bd_1
  matplotlib-base-3.3.2-py38h5c7f4ab_1
  mistune-0.8.4-py38h1e0a361_1002
  mkl-2020.4-h726a3e6_304
  mysql-common-8.0.21-2
  mysql-libs-8.0.21-hf3661c5_2
  nb_conda_kernels-2.3.0-py38h32f6830_3
  nbclient-0.5.1-py_0
  nbconvert-6.0.7-py38h32f6830_2
  nbformat-5.0.8-py_0
  ncurses-6.2-h58526e2_3
  nest-asyncio-1.4.2-pyhd8ed1ab_0
  nettle-3.4.1-h1bed415_1002
  networkx-2.5-py_0
  ninja-1.10.1-hfc4b9b4_2
  notebook-6.1.5-py38h578d9bd_0
  nspr-4.29-he1b5a44_1
  nss-3.58-h27285de_1
  numba-0.51.2-py38hc5bc63f_0
  numpy-1.19.4-py38hf0fd68c_1
  olefile-0.46-pyh9f0ad1d_1
  opencv-4.5.0-py38_2
  openh264-2.1.1-h8b12597_0
  openssl-1.1.1h-h516909a_0
  packaging-20.4-pyh9f0ad1d_0
  pandoc-2.11.0.4-hd18ef5c_0
  pandocfilters-1.4.2-py_1
  parso-0.7.1-pyh9f0ad1d_0
  pcre-8.44-he1b5a44_0
  pexpect-4.8.0-pyh9f0ad1d_2
  pickleshare-0.7.5-py_1003
  pillow-8.0.1-py38h70fbd49_0
  pip-20.2.4-py_0
  pixman-0.40.0-h36c2ea0_0
  pooch-1.2.0-py_0
  prometheus_client-0.8.0-pyh9f0ad1d_0
  prompt-toolkit-3.0.8-pyha770c72_0
  prompt_toolkit-3.0.8-hd8ed1ab_0
  pthread-stubs-0.4-h14c3975_1001
  ptyprocess-0.6.0-py_1001
  py-opencv-4.5.0-py38h1cdfbd6_2
  pycparser-2.20-pyh9f0ad1d_2
  pygments-2.7.2-py_0
  pyopenssl-19.1.0-py_1
  pyparsing-2.4.7-pyh9f0ad1d_0
  pyqt-5.12.3-py38ha8c2ead_4
  pyrsistent-0.17.3-py38h1e0a361_1
  pysocks-1.7.1-py38h924ce5b_2
  pysoundfile-0.10.2-py_1001
  python-3.8.6-h852b56e_0_cpython
  python-dateutil-2.8.1-py_0
  python_abi-3.8-1_cp38
  pytorch-1.7.0-py3.8_cpu_0
  pyzmq-19.0.2-py38ha71036d_2
  qt-5.12.9-h1f2b2cb_0
  qtconsole-4.7.7-pyh9f0ad1d_0
  qtpy-1.9.0-py_0
  readline-8.0-he28a2e2_2
  requests-2.24.0-pyh9f0ad1d_0
  resampy-0.2.2-py_0
  scikit-learn-0.23.2-py38h5d63f67_2
  scipy-1.5.3-py38h828c644_0
  send2trash-1.5.0-py_0
  setuptools-49.6.0-py38h924ce5b_2
  six-1.15.0-pyh9f0ad1d_0
  sqlite-3.33.0-h4cf870e_1
  terminado-0.9.1-py38h32f6830_1
  testpath-0.4.4-py_0
  threadpoolctl-2.1.0-pyh5ca1d4c_0
  tk-8.6.10-hed695b0_1
  torchtext-0.8.0-py38
  torchvision-0.8.1-py38_cpu
  tornado-6.1-py38h25fe258_0
  tqdm-4.51.0-pyh9f0ad1d_0
  traitlets-5.0.5-py_0
  typing_extensions-3.7.4.3-py_0
  urllib3-1.25.11-py_0
  wcwidth-0.2.5-pyh9f0ad1d_2
  webencodings-0.5.1-py_1
  wheel-0.35.1-pyh9f0ad1d_0
  widgetsnbextension-3.5.1-py38h32f6830_4
  x264-1!152.20180806-h14c3975_0
  xorg-kbproto-1.0.7-h14c3975_1002
  xorg-libice-1.0.10-h516909a_0
  xorg-libsm-1.2.3-h84519dc_1000
  xorg-libx11-1.6.12-h516909a_0
  xorg-libxau-1.0.9-h14c3975_0
  xorg-libxdmcp-1.1.3-h516909a_0
  xorg-libxext-1.3.4-h516909a_0
  xorg-libxrender-0.9.10-h516909a_1002
  xorg-renderproto-0.11.1-h14c3975_1002
  xorg-xextproto-7.3.0-h14c3975_1002
  xorg-xproto-7.0.31-h14c3975_1007
  xz-5.2.5-h516909a_1
  zeromq-4.3.3-he1b5a44_2
  zipp-3.4.0-py_0
  zlib-1.2.11-h516909a_1010
  zstd-1.4.5-h6597ccf_2


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: | b'Config option `kernel_spec_manager_class` not recognized by `UninstallNBExtensionApp`.\nUninstalling jupyter-js-widgets jupyter-js-widgets/extension\nRemoving: /home/phunc20/.config/miniconda3/envs/abc/share/jupyter/nbextensions/jupyter-js-widgets\n'
\ b'Disabling nb_conda_kernels...\nStatus: disabled\n'
done
[phunc20@homography-x220t pytorch-Deep-Learning]$ conda info --envs
# conda environments:
#
base                  *  /home/phunc20/.config/miniconda3
pDL                      /home/phunc20/.config/miniconda3/envs/pDL

[phunc20@homography-x220t pytorch-Deep-Learning]$ conda env remove --name pDL

Remove all packages in environment /home/phunc20/.config/miniconda3/envs/pDL:

[phunc20@homography-x220t pytorch-Deep-Learning]$ conda info --envs
# conda environments:
#
base                  *  /home/phunc20/.config/miniconda3
```
