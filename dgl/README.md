## Installation of `dgl`
- `requests` package, I found out, if we don't install it, Python will complain when we import `dgl`.

```bash
# Create a conda env
conda create -n dgl python=3.7

# https://www.dgl.ai/pages/start.html
conda install -n dgl -c dglteam dgl

# https://pytorch.org/get-started/locally/
conda install -n dgl pytorch torchvision torchaudio cpuonly -c pytorch

conda install -n dgl requests
```

