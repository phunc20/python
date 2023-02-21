## Version
Often, when installing packages related to PyTorch, we get those options specifying
different installation paths according to CUDA version.

Assuming that you've already had PyTorch installed, a way to know CUDA version is
```bash
$ python -c "import torch; print(torch.version.cuda)"
11.3
```

Also note that the result is different from the following:
```bash
$ nvidia-smi | grep -i version
| NVIDIA-SMI 525.85.05    Driver Version: 525.85.05    CUDA Version: 12.0     |
```

