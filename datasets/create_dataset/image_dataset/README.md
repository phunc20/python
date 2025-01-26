# Create Image Dataset in HuggingFace's `datasets`
At the time of writing this file, there are basically two methods to create
an image dataset in `datasets`:

1. `"imagefolder"`: This seems to be only suitable for smaller image dataset.
   The official doc says that
   > `"imagefolder"` _is designed to quickly load an image dataset with **several thousand images** without requiring you to write any code_.
2. `"webdataset"`: This seems to allow loading of larger image dataset.


## ImageFolder
I will show an example to illustrate roughly the process.

```bash
phunc20@daikon:~/git-repos/huggingface_hub/phunc20/nj_biergarten_captcha_v2$ ls
test  train  validation
phunc20@daikon:~/git-repos/huggingface_hub/phunc20/nj_biergarten_captcha_v2$ ls train/ | wc -l
20000
phunc20@daikon:~/git-repos/huggingface_hub/phunc20/nj_biergarten_captcha_v2$ ls validation/ | wc -l
300
phunc20@daikon:~/git-repos/huggingface_hub/phunc20/nj_biergarten_captcha_v2$ ls test/ | wc -l
500
phunc20@daikon:~/git-repos/huggingface_hub/phunc20/nj_biergarten_captcha_v2$ ls train/ | head -n 3
2024-12-30T14:48:46_flf1gm.jpg
2024-12-30T14:48:48_rt3168.jpg
2024-12-30T14:49:46_thu8mm.jpg
phunc20@daikon:~/git-repos/huggingface_hub/phunc20/nj_biergarten_captcha_v2$ ls validation/ | head -n 3
2024-12-30T19:13:53_35j5ti.jpg
2024-12-30T19:50:54_ab7prf.jpg
2025-01-04T17:57:10_tv3wr4.jpg
phunc20@daikon:~/git-repos/huggingface_hub/phunc20/nj_biergarten_captcha_v2$ ls test/ | head -n 3
2024-12-30T16:44:05_9ymyht.jpg
2024-12-30T17:01:38_nilr3w.jpg
2024-12-30T17:02:57_fl9kyd.jpg

(nj_biergarten) phunc20@daikon:~/git-repos/huggingface_hub/phunc20/nj_biergarten_captcha_v2$ conda activate nj_biergarten
(nj_biergarten) phunc20@daikon:~/git-repos/huggingface_hub/phunc20/nj_biergarten_captcha_v2$ ipython
Python 3.10.12 (main, Jul  5 2023, 18:54:27) [GCC 11.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.31.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from datasets import load_dataset

In [2]: dataset = load_dataset("imagefolder", data_dir="nj_biergarten_captcha_v2", drop_labels=True)
Resolving data files: 100%|██████████████████████████████████████████████████████████████████████| 20000/20000 [00:00<00:00, 23445.27it/s]
Resolving data files: 100%|██████████████████████████████████████████████████████████████████████████| 300/300 [00:00<00:00, 19663.26it/s]
Resolving data files: 100%|██████████████████████████████████████████████████████████████████████████| 500/500 [00:00<00:00, 17467.24it/s]
Downloading data: 100%|███████████████████████████████████████████████████████████████████████| 20000/20000 [00:00<00:00, 58571.40files/s]
Downloading data: 100%|███████████████████████████████████████████████████████████████████████████| 300/300 [00:00<00:00, 22077.61files/s]
Downloading data: 100%|███████████████████████████████████████████████████████████████████████████| 500/500 [00:00<00:00, 19755.75files/s]
Generating train split: 20000 examples [00:01, 19300.26 examples/s]
Generating validation split: 300 examples [00:00, 17929.23 examples/s]
Generating test split: 500 examples [00:00, 18732.93 examples/s]

In [3]: dataset
Out[3]:
DatasetDict({
    train: Dataset({
        features: ['image'],
        num_rows: 20000
    })
    validation: Dataset({
        features: ['image'],
        num_rows: 300
    })
    test: Dataset({
        features: ['image'],
        num_rows: 500
    })
})

In [4]: from pathlib import Path

In [5]: def get_label(fpath: Path) -> str:
   ...:     return fpath.stem.split("_")[-1]
   ...:

In [6]: def add_label(example):
   ...:     p = Path(example["image"].filename)
   ...:     label = get_label(p)
   ...:     example["label"] = label
   ...:     return example
   ...:

In [7]: for k, v in dataset.items():
   ...:     dataset[k] = v.map(add_label)
   ...:
Map: 100%|█████████████████████████████████████████████████████████████████████████████████| 20000/20000 [00:11<00:00, 1751.63 examples/s]
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 300/300 [00:00<00:00, 463.40 examples/s]
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 500/500 [00:00<00:00, 635.84 examples/s]

In [8]: dataset
Out[8]:
DatasetDict({
    train: Dataset({
        features: ['image', 'label'],
        num_rows: 20000
    })
    validation: Dataset({
        features: ['image', 'label'],
        num_rows: 300
    })
    test: Dataset({
        features: ['image', 'label'],
        num_rows: 500
    })
})

In [9]: dataset["train"][0]["image"]
Out[9]: <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=140x50>

In [10]: dataset["train"][0]["label"]
Out[10]: 'flf1gm'

In [11]: import matplotlib.pyplot as plt

In [12]: plt.imshow(dataset["train"][0]["image"])
Out[12]: <matplotlib.image.AxesImage at 0x7f8d466c3700>

In [13]: plt.show()
```


## WebDataset
Similarly, we use an example to illustrate this method:

```bash
phunc20@daikon:~/git-repos/huggingface_hub/phunc20$ ls nj_biergarten_captcha/
001.tar  002.tar
phunc20@daikon:~/git-repos/huggingface_hub/phunc20$ du -hsx nj_biergarten_captcha/*
675M    nj_biergarten_captcha/001.tar
675M    nj_biergarten_captcha/002.tar
phunc20@daikon:~/git-repos/huggingface_hub/phunc20$ tar tvf nj_biergarten_captcha/001.tar | wc -l
238119
phunc20@daikon:~/git-repos/huggingface_hub/phunc20$ tar tvf nj_biergarten_captcha/002.tar | wc -l
238001
phunc20@daikon:~/git-repos/huggingface_hub/phunc20$ tar tvf nj_biergarten_captcha/001.tar | head -n 5
drwxr-xr-x phunc20/wheel     0 2025-01-14 13:31 001/
-rw-r--r-- phunc20/wheel  1867 2024-10-08 18:21 001/2024-10-08T18:21:10.578994_y2jhuv.jpg
-rw-r--r-- phunc20/wheel  2004 2024-10-08 18:21 001/2024-10-08T18:21:11.844534_34veh5.jpg
-rw-r--r-- phunc20/wheel  1867 2024-10-08 18:21 001/2024-10-08T18:21:13.102441_utem6a.jpg
-rw-r--r-- phunc20/wheel  1946 2024-10-08 18:21 001/2024-10-08T18:21:14.304472_h32d87.jpg
phunc20@daikon:~/git-repos/huggingface_hub/phunc20$ tar tvf nj_biergarten_captcha/002.tar | head -n 5
drwxr-xr-x phunc20/phunc20   0 2025-01-14 13:31 002/
-rw-r--r-- phunc20/wheel  2523 2025-01-12 07:25 002/2025-01-12T07:25:19.869257_pxvesu.jpg
-rw-r--r-- phunc20/wheel  1994 2025-01-13 04:04 002/2025-01-13T04:04:25.970852_1lht9j.jpg
-rw-r--r-- phunc20/wheel  2095 2025-01-10 23:45 002/2025-01-10T23:45:02.513022_a7lsoj.jpg
-rw-r--r-- phunc20/phunc20 1618 2025-01-14 01:22 002/2025-01-14T01:22:08.099094_mztiur.jpg
phunc20@daikon:~/git-repos/huggingface_hub/phunc20$ conda activate nj_biergarten
(nj_biergarten) phunc20@daikon:~/git-repos/huggingface_hub/phunc20$ ipython
Python 3.10.12 (main, Jul  5 2023, 18:54:27) [GCC 11.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.31.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from datasets import load_dataset

In [2]: dataset = load_dataset("webdataset", data_dir="nj_biergarten_captcha")
Generating train split: 476118 examples [02:37, 3029.21 examples/s]

In [3]: dataset
Out[3]:
DatasetDict({
    train: Dataset({
        features: ['__key__', '__url__', 'jpg'],
        num_rows: 476118
    })
})

In [4]: dataset["train"][0]["__key__"]
Out[4]: '001/2024-10-08T18:21:10.578994_y2jhuv'

In [5]: dataset["train"][0]["__url__"]
Out[5]: '/home/phunc20/git-repos/huggingface_hub/phunc20/nj_biergarten_captcha/001.tar'

In [6]: dataset["train"][0]["jpg"]
Out[6]: <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=140x50>
```


## Ref.
- <https://huggingface.co/docs/datasets/en/image_dataset>
- <https://webdataset.github.io/webdataset/>
