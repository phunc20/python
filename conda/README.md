
- [https://conda.io/miniconda.html](https://conda.io/miniconda.html)
```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```


```bash
[phunc20@denjiro-x220 pytorch-Deep-Learning]$ conda env create -f environment.yml
Collecting package metadata (repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.8.3
  latest version: 4.9.0

Please update conda by running

    $ conda update -n base -c defaults conda



Downloading and Extracting Packages
c-ares-1.16.1        | 107 KB    | ############################################################################### | 100%
libgcc-ng-9.3.0      | 7.8 MB    | ############################################################################### | 100%
bzip2-1.0.8          | 398 KB    | ############################################################################### | 100%
ipywidgets-7.5.1     | 101 KB    | ############################################################################### | 100%
ld_impl_linux-64-2.3 | 617 KB    | ############################################################################### | 100%
pyzmq-19.0.2         | 511 KB    | ############################################################################### | 100%
libpng-1.6.37        | 359 KB    | ############################################################################### | 100%
nspr-4.29            | 232 KB    | ############################################################################### | 100%
dgl-0.5.2            | 3.3 MB    | ############################################################################### | 100%
jasper-1.900.1       | 286 KB    | ############################################################################### | 100%
...

ffmpeg-4.3.1         | 83.4 MB   | ###############################################################################[12/260]
Preparing transaction: done
Verifying transaction: done
Executing transaction: | b'Enabling nb_conda_kernels...\nStatus: enabled\n'
done
Ran pip subprocess with arguments:
['/home/phunc20/miniconda3/envs/pDL/bin/python', '-m', 'pip', 'install', '-U', '-r', '/home/phunc20/git-repos/github/Atcol
d/pytorch-Deep-Learning/condaenv.58us3wbo.requirements.txt']
Pip subprocess output:
Collecting torchviz
  Downloading torchviz-0.0.1.tar.gz (41 kB)
Requirement already satisfied, skipping upgrade: torch in /home/phunc20/miniconda3/envs/pDL/lib/python3.8/site-packages (f
rom torchviz->-r /home/phunc20/git-repos/github/Atcold/pytorch-Deep-Learning/condaenv.58us3wbo.requirements.txt (line 1))
(1.6.0)
Collecting graphviz
  Downloading graphviz-0.14.2-py2.py3-none-any.whl (18 kB)
Processing /home/phunc20/.cache/pip/wheels/8e/70/28/3d6ccd6e315f65f245da085482a2e1c7d14b90b30f239e2cf4/future-0.18.2-py3-n
one-any.whl
Requirement already satisfied, skipping upgrade: numpy in /home/phunc20/miniconda3/envs/pDL/lib/python3.8/site-packages (f
rom torch->torchviz->-r /home/phunc20/git-repos/github/Atcold/pytorch-Deep-Learning/condaenv.58us3wbo.requirements.txt (li
ne 1)) (1.19.2)
Building wheels for collected packages: torchviz
  Building wheel for torchviz (setup.py): started
  Building wheel for torchviz (setup.py): finished with status 'done'
  Created wheel for torchviz: filename=torchviz-0.0.1-py3-none-any.whl size=3520 sha256=fd04541fe13f54dac0eda6daf4065511c5
e240ebf4c01b5f5b04a5fd3f4e70e2
  Stored in directory: /home/phunc20/.cache/pip/wheels/89/b0/3c/fd769174401ef5d43e18d047b509b91f8635f8fba6dacaf4f6
Successfully built torchviz
Installing collected packages: graphviz, torchviz, future
Successfully installed future-0.18.2 graphviz-0.14.2 torchviz-0.0.1

#
# To activate this environment, use
#
#     $ conda activate pDL
#
# To deactivate an active environment, use
#
#     $ conda deactivate

[phunc20@denjiro-x220 pytorch-Deep-Learning]$ vim ~/todos/
```





```bash
(base) [phunc20@denjiro-x220 ~]$ conda config --show
add_anaconda_token: True
add_pip_as_python_dependency: True
aggressive_update_packages:
  - ca-certificates
  - certifi
  - openssl
allow_conda_downgrades: False
allow_cycles: True
allow_non_channel_urls: False
allow_softlinks: False
always_copy: False
always_softlink: False
always_yes: None
anaconda_upload: None
auto_activate_base: True
auto_stack: 0
auto_update_conda: True
bld_path:
...
use_only_tar_bz2: False
verbosity: 0
verify_threads: 1
whitelist_channels: []
(base) [phunc20@denjiro-x220 ~]$
```
