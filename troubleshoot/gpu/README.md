## CUDA
The most used DL frameworks by myself were `tensorflow` (or `tf` for short) and `pytorch`. And my used-to-be favorite python package manager had been `pip`.

But with `tf` and `pip`, there was this CUDA version problem. That is,
- as of year 2020/2021, on a Fedora33 machine, I installed CUDA11 (via `dnf install xorg-x11-drv-nvidia-cuda`) on a laptop equipped with an `NVIDIA Corporation GP104M [GeForce GTX 1070 Mobile]`, both gpu versions of `tf1` and `tf2` installed via `pip` complained about not being able to find the proper cuda library, versions `cuda11.0` and `cuda10.0`, resp. This despite the fact that I had CUDA11 on this machine and `pytorch` (installed via `pip` as well) ran perfectly with GPU activated.
- Year 2019, I had the same laptop with Ubunt18.04 and CUDA10 installed on it. It somehow configured to be able to use `tf1` (via `pip`), but reported problem using `tf2` with GPU, because it needed CUDA11.

All these were just kind of complicated, and not pretty well documented -- Installing multiple CUDA versions seemed to be possible but seemed difficult and unstable.

## Solution
At first, I did not like Anaconda very much, thinking that a package manager should be sth possessed by a single company. But the DL course by `atcold` from NYU was great and it used `miniconda`, so I tried in year 2020, finding it not bad. This time, I tried my luck with GPU and `miniconda`.

It turned out that when you asked `miniconda` to install some version of `tf`, it will install sth called `cudatoolkit` and that seems to cover the problem of CUDA versions. Each `tf` package inside an environment has its own `cudatoolkit`, no problem running `tf` anymore.
```bash
~ ❯❯❯ conda create -n tf1
~ ❯❯❯ condact tf1
(tf1) ~ ❯❯❯ conda install -n tf1 tensorflow-gpu=1.13.1
Collecting package metadata (current_repodata.json): done                                                                                                     
Solving environment: failed with initial frozen solve. Retrying with flexible solve.                                                                          
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/phunc20/.config/miniconda3/envs/tf1

  added / updated specs:

    - tensorflow-gpu=1.13.1

The following packages will be downloaded:

    package                    |            build
    ---------------------------|----------------- 
    astor-0.8.1                |           py37_0          47 KB
    certifi-2020.12.5          |   py37h06a4308_0         141 KB
    cudatoolkit-10.0.130       |                0       261.2 MB
    cudnn-7.6.5                |       cuda10.0_0       165.0 MB
    cupti-10.0.130             |                0         1.5 MB
    gast-0.4.0                 |             py_0          15 KB
    grpcio-1.31.0              |   py37hf8bcb03_0         2.0 MB
    h5py-2.10.0                |   py37hd6299e0_1         902 KB
    keras-applications-1.0.8   |             py_1          29 KB
    markdown-3.3.3             |   py37h06a4308_0         127 KB
    mkl-service-2.3.0          |   py37he8ac12f_0          52 KB
    mkl_fft-1.2.0              |   py37h23d657b_0         148 KB
    mkl_random-1.1.1           |   py37h0573a6f_0         322 KB
    mock-4.0.3                 |     pyhd3eb1b0_0          29 KB
    numpy-1.19.2               |   py37h54aff64_0          22 KB
    numpy-base-1.19.2          |   py37hfa32c7d_0         4.1 MB
    pip-20.3.3                 |   py37h06a4308_0         1.8 MB
    protobuf-3.13.0.1          |   py37he6710b0_1         634 KB
    python-3.7.9               |       h7579374_0        45.3 MB
    scipy-1.5.2                |   py37h0b6359f_0        14.3 MB
    setuptools-51.1.2          |   py37h06a4308_4         739 KB
    six-1.15.0                 |   py37h06a4308_0          27 KB
    tensorboard-1.13.1         |   py37hf484d3e_0         3.1 MB
    tensorflow-1.13.1          |gpu_py37hc158e3b_0           4 KB
    tensorflow-base-1.13.1     |gpu_py37h8d69cac_0       130.2 MB
    tensorflow-estimator-1.13.0|             py_0         181 KB
    tensorflow-gpu-1.13.1      |       h0d30ee6_0           3 KB
    termcolor-1.1.0            |           py37_1           8 KB
    ------------------------------------------------------------
                                           Total:       631.9 MB
```
