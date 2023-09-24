## Build from Source
In my own use case, I had a Thinkpad X61s that, at the time of writing,
I used quite often. For a long period of time, I had temporarily given
up to develop anything `tensorflow>1.5` on this machine because most
`pip`-installed TensorFlow versions after 1.5 seemed to be compiled
on more advanced CPUs (in particular with AVX), resulting in
```
$ python -c "import tensorflow"
Illegal instruction (core dumped)
```

I have always been told to have to compile/build from source for the
particular CPU structure of my machine, but never quite found time to
successfully do so. Not until I found out that
1. `pandas`, say, version 2.1.0, also `core dumped` on Thinkpad X61s
2. `tensorflow` and `pandas` on Thinkpad X61s can both be **correctly
   installed via `conda`**!
    - It seems that `conda` provides many different compiled versions
      than `pip`
    - One can specify right at the moment of creating a virtual environment
      ```bash
      $ conda create -c conda-forge -n py3.10 python pandas tensorflow
      ```


Unfortunately, as of 2023/09/24, `conda` does not provide `tensorflow-text`
and `pip install tensorflow-text` core dumped on Thinkpad X61s. Luckily,
one can still build `tensorflow-text` from source. Here is how:

1. Create a Python virtual environment via conda
   ```bash
   $ conda create -c conda-forge -n py3.11 python pandas tensorflow
   ```
1. Git pull back `tensorflow-text`, tags, `co v2.12.0`
1. You need to have `bazel` installed. Follow the instructions on TensorFlow's
   official website or from the wiki of your Linux distro.
1. Normally one only needs to run
   (e.g. if we target to install `tensorflow-text==2.12.0`)
   ```bash
   ~ $ mkcd ~/git-repos/github/tensorflow/
   github/tensorflow $ git clone https://github.com/tensorflow/text.git
   github/tensorflow $ cd text/
   tensorflow/text $ git fetch --all --tags --prune
   tensorflow/text $ git checkout v2.12.0
   tensorflow/text $ conda activate py3.11
   (py3.11) tensorflow/text $ ./oss_scripts/run_build.sh
   ```
   Then after the compilation successfully finishes, there will be a wheel file
   `tensorflow_text-<tf_text_version>-<cpython_version>-<cpython_version>-<os>.whl`,
   like described in the `README.md`. After that, it suffices to, e.g.
   ```bash
   (py3.11) tensorflow/text $ pip install tensorflow_text-2.12.0-cp311-cp311-linux_x86_64.whl
   (py3.11) tensorflow/text $ cd
   (py3.11) ~ $ python -c "import tensorflow_text as tf_text; print(f'{tf_text.__version__ = }')"
   tf_text.__version__ = '2.12.0'
   (py3.11) ~ $ # Note we've changed directory before testing to avoid namespace confusion
   (py3.11) ~ $ 
   ```
   **But**, there is always a but. And that is, in my case, the compilation
   process wasn't that easy. Let's read on.
    - Rmk. The reason we chose to install `tensorflow-text==2.12.0` was that,
      at the time of writing, the latest `tensorflow` availabel version on
      `conda` was `2.12.0` and that `tensorflow-text` version should
      coincide with `tensorflow` version.
1. I am no expert of TensorFlow compilation or of bazel. But here are a few
   of the most important files I notice when it comes to building `tensorflow-text`
   from source
   ```bash
   WORKSPACE
   .bazelversion
   oss_scripts/prepare_tf_dep.sh
   oss_scripts/run_build.sh
   ```
    - `WORKSPACE` seems to contain package information for `bazel` to
      download and cache for the purpose of compilation.
    - `.bazelversion` will contain the `bazel` version, of course. what
      is less obvious is that the version in this file seems to be determined
      by the content of `WORKSPACE`
    - `oss_scripts/prepare_tf_dep.sh` will collect package versions dynamically
      and will overwrite the `WORKSPACE` file. However, since our `tensorflow`
      was installed via `conda` instead of via `pip` or via compiling from source,
      the `tf.__git_version__` will be empty string
      (You could try `import numpy as np; print(f'{np.__git_version__ = }')`
      if you want to see how it should look like). For another thing, under the
      Git commit tag `v2.12.0`, the default `WORKSPACE` file's content looks
      like already taken care of, so eventually I have decided to remove many
      lines from `oss_scripts/prepare_tf_dep.sh`, more precisely, line 23 until EOF.
    - `oss_scripts/run_build.sh` has also one line that needs to be modified
      (because its content is more than just a version number, containing a comment)
      ```
      -tf_bazel_version=$(cat .bazelversion)
      +tf_bazel_version=$(head -1 .bazelversion)
      ```
    - Once these modifications done, go back to the compilation steps above, and it
      should compile just fine.
