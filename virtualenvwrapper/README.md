# <code>virtualenvwrapper</code>
Here are a few steps to have <code>virtualenvwrapper</code> work on a general Linux machine:
- <code><b>pip install --user virtualenv virtualenvwrapper</b></code> (The <code>--user</code> option will configure the system to install to <code><b>~/.local/bin</b></code> instead of some system-wise path, in other words, specific to the current user)
    ```bash
    [phunc20@headache-x220tablet ~]$ pip
    pip     pip3    pip3.7  pip3.8
    [phunc20@headache-x220tablet ~]$ pip3.7 install --user virtualenv
    Collecting virtualenv
      Downloading virtualenv-20.0.31-py2.py3-none-any.whl (4.9 MB)
         |████████████████████████████████| 4.9 MB 827 kB/s
    Collecting filelock<4,>=3.0.0
      Downloading filelock-3.0.12-py3-none-any.whl (7.6 kB)
    Collecting appdirs<2,>=1.4.3
      Downloading appdirs-1.4.4-py2.py3-none-any.whl (9.6 kB)
    Collecting distlib<1,>=0.3.1
      Downloading distlib-0.3.1-py2.py3-none-any.whl (335 kB)
         |████████████████████████████████| 335 kB 8.7 MB/s
    Collecting six<2,>=1.9.0
      Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
    Collecting importlib-metadata<2,>=0.12; python_version < "3.8"
      Downloading importlib_metadata-1.7.0-py2.py3-none-any.whl (31 kB)
    Collecting zipp>=0.5
      Downloading zipp-3.1.0-py3-none-any.whl (4.9 kB)
    Installing collected packages: filelock, appdirs, distlib, six, zipp, importlib-metadata, virtualenv
    Successfully installed appdirs-1.4.4 distlib-0.3.1 filelock-3.0.12 importlib-metadata-1.7.0 six-1.15.0 virtualenv-20.0.31 zipp-3.1.0
    WARNING: You are using pip version 20.1.1; however, version 20.2.2 is available.
    You should consider upgrading via the '/usr/local/bin/python3.7 -m pip install --upgrade pip' command.
    [phunc20@headache-x220tablet ~]$ pip3.7 install --user virtualenvwrapper
    Collecting virtualenvwrapper
      Downloading virtualenvwrapper-4.8.4.tar.gz (334 kB)
         |████████████████████████████████| 334 kB 957 kB/s
    Requirement already satisfied: virtualenv in ./.local/lib/python3.7/site-packages (from virtualenvwrapper) (20.0.31)
    Collecting virtualenv-clone
      Downloading virtualenv_clone-0.5.4-py2.py3-none-any.whl (6.6 kB)
    Collecting stevedore
      Downloading stevedore-3.2.0-py3-none-any.whl (42 kB)
         |████████████████████████████████| 42 kB 658 kB/s
    Requirement already satisfied: distlib<1,>=0.3.1 in ./.local/lib/python3.7/site-packages (from virtualenv->virtualenvwrapper) (0.3.1)
    Requirement already satisfied: importlib-metadata<2,>=0.12; python_version < "3.8" in ./.local/lib/python3.7/site-packages (from virtualenv->virtualenvwrapper) (1.7.0)
    Requirement already satisfied: appdirs<2,>=1.4.3 in ./.local/lib/python3.7/site-packages (from virtualenv->virtualenvwrapper) (1.4.4)
    Requirement already satisfied: six<2,>=1.9.0 in ./.local/lib/python3.7/site-packages (from virtualenv->virtualenvwrapper) (1.15.0)
    Requirement already satisfied: filelock<4,>=3.0.0 in ./.local/lib/python3.7/site-packages (from virtualenv->virtualenvwrapper) (3.0.12)
    Collecting pbr!=2.1.0,>=2.0.0
      Using cached pbr-5.4.5-py2.py3-none-any.whl (110 kB)
    Requirement already satisfied: zipp>=0.5 in ./.local/lib/python3.7/site-packages (from importlib-metadata<2,>=0.12; python_version < "3.8"->virtualenv->virtualenvwrapper) (3.1.0)
    Using legacy setup.py install for virtualenvwrapper, since package 'wheel' is not installed.
    Installing collected packages: virtualenv-clone, pbr, stevedore, virtualenvwrapper
        Running setup.py install for virtualenvwrapper ... done
    Successfully installed pbr-5.4.5 stevedore-3.2.0 virtualenv-clone-0.5.4 virtualenvwrapper-4.8.4
    WARNING: You are using pip version 20.1.1; however, version 20.2.2 is available.
    You should consider upgrading via the '/usr/local/bin/python3.7 -m pip install --upgrade pip' command.
    [phunc20@headache-x220tablet ~]$ tree -L 2 .local/
    .local/
    ├── bin
    │   ├── bright-down
    │   ├── bright-up
    │   ├── ez_dwmbar
    │   ├── pbr
    │   ├── refbar
    │   ├── v
    │   ├── vifmimg
    │   ├── virtualenv
    │   ├── virtualenv-clone
    │   ├── virtualenvwrapper_lazy.sh
    │   └── virtualenvwrapper.sh
    ├── lib
    │   └── python3.7
    └── share
        ├── nvim
        ├── sx
        ├── vifm
        └── xorg
    
    8 directories, 11 files
    ```
- Put the following text into <code><b>.bashrc</b></code>, save it and, finally, <code><b>source</b></code> it.
    ```bash
    ## For python virtualenvwrapper
    export WORKON_HOME="$HOME/.virtualenvs"
    #export VIRTUALENVWRAPPER_PYTHON="/usr/bin/python3"
    export VIRTUALENVWRAPPER_PYTHON="$(which python3.7)"
    source "$HOME/.local/bin/virtualenvwrapper.sh"
    ```
- When you finish <code><b>source ~/.bashrc</b></code>, you should see
    ```bash
    [phunc20@headache-x220tablet ~]$ source ~/.bashrc
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/premkproject
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/postmkproject
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/initialize
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/premkvirtualenv
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/postmkvirtualenv
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/prermvirtualenv
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/postrmvirtualenv
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/predeactivate
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/postdeactivate
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/preactivate
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/postactivate
    virtualenvwrapper.user_scripts creating /home/phunc20/.virtualenvs/get_env_details
    ```
- Now, <code><b>virtualenvwrapper</b></code> has been correctly installed. Here are a few tips to use it.
    - To create a new environment (specifying the python version),
    	- <code><b>mkvirtualenv -p \<python-version\> \<your-named-env\></b></code>
    	- <code><b>mkvirtualenv -p python3.7 my-py37-env</b></code> 
    	- <code><b>mkvirtualenv -p python3.8 my-py38-env</b></code>
    - To <b>activate</b> a previously built environment,
        - <code><b>workon my-py37-env</b></code>
    - To <b>get out</b> of the current environment,
        - <code><b>deactivate</b></code>

## Arch-Linux specific
Due to the rolling-release nature of Arch-based distros, installing `virtualenvwrapper` like above will encounter a problem: When the system's default Python gets upgraded (e.g. from `python3.8` to `python3.9` via `pacman -Syu`), the already installed virtual environments will all become useless.

One remedy to this problem is to install a diff version of python on arch-based machine, say `python3.7` (cf. `../installation/from-source/README.md`). Then `pip3.7 install virtualenvwrapper` in that version of python and remember to set the environment variable to that version of python on your machine as well.
```bash
## For python virtualenvwrapper
export WORKON_HOME="$HOME/.virtualenvs"
#export VIRTUALENVWRAPPER_PYTHON="$(which python3.8)"
export VIRTUALENVWRAPPER_PYTHON="$(which python3.7)"
source "$HOME/.local/bin/virtualenvwrapper.sh"
```


