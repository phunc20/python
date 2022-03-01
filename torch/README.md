## GPU
To check whether your `torch` is compiled with GPU, use the following command

- `torch.cuda.is_available()`
    - When there is GPU
      ```python
      In [3]: torch.cuda.is_available()
      Out[3]: True
      
      In [4]: torch.cuda.current_device()
      Out[4]: 0
      
      In [6]: torch.cuda.device_count()
      Out[6]: 1
      
      In [7]: torch.cuda.get_device_name()
      Out[7]: 'Tesla T4'
      
      In [8]: torch.cuda.get_device_capability()
      Out[8]: (7, 5)
      
      In [9]: torch.cuda.get_device_properties()
      TypeError: get_device_properties() missing 1 required positional argument: 'device'
      
      In [10]: torch.cuda.get_device_properties(0)
      Out[10]: _CudaDeviceProperties(name='Tesla T4', major=7, minor=5, total_memory=15109MB, multi_processor_count=40)
      
      In [11]: torch.cuda.get_device_properties(torch.cuda.current_device())
      Out[11]: _CudaDeviceProperties(name='Tesla T4', major=7, minor=5, total_memory=15109MB, multi_processor_count=40)
      
      In [12]: torch.cuda.get_device_name(torch.cuda.current_device())
      Out[12]: 'Tesla T4'
      
      In [13]: torch.cuda.get_device_capability(torch.cuda.current_device())
      Out[13]: (7, 5)
      ```
    - When there is no GPU
      ```python
      In [4]: torch.cuda.is_available()
      Out[4]: False
      
      In [5]: torch.cuda.current_device()
      AssertionError: Torch not compiled with CUDA enabled
      
      In [7]: torch.cuda.device_count()
      Out[7]: 0
      
      In [8]: torch.cuda.get_device_name(0)
      AssertionError: Torch not compiled with CUDA enabled
      ```
