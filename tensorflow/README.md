## GPU
To check whether your `tf` is compiled with GPU, use the following command

- `tf.config.list_physical_devices("GPU")`
    - When there is GPU
      ```python
      In [2]: tf.config.list_physical_devices("GPU")
      2022-03-01 06:16:44.704574: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:936] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
      2022-03-01 06:16:44.705271: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:936] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
      2022-03-01 06:16:44.705886: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:936] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
      Out[2]: [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
      ```
    - When there is no GPU
      ```python
      In [2]: tf.config.list_physical_devices("GPU")
      2022-03-01 13:22:43.830085: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library
      'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
      2022-03-01 13:22:43.830123: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)
      2022-03-01 13:22:43.830168: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be
      running on this host (mushroom-x200): /proc/driver/nvidia/version does not exist
      Out[2]: []
      ```
- (deprecated) `tf.test.is_gpu_available()`
