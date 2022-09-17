




By default, `tensorflow` will run on GPU, if your machine have one and configured so.
To have it run on CPU instead, one can do as follows.
```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
```

To verify whether `tensorflow` is running on GPU:
```python
# For older tf2 releases
tf.test.is_gpu_available()
# For newer tf2 releases
tf.config.list_physical_devices("GPU")
```

For example,
- w/o GPU
  ```python
  In [3]: tf.config.list_physical_devices("GPU")
  Out[3]: []
  ```
- w/ GPU
  ```python
  In [3]: tf.config.list_physical_devices("GPU")
  2022-09-17 13:17:53.646935: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:975] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
  2022-09-17 13:17:53.647276: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:975] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
  2022-09-17 13:17:53.647507: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:975] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
  Out[3]: [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
  ```
