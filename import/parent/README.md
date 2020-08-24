# How to "<code>import</code> scripts" from parent directory?
This repository's structure is as follows.

```python
(rlcomp2020-tf2) [phunc20@artichaut-x220 parent]$ tree .
.
├── child
│   └── use_constants.py
└── constants.py

1 directory, 2 files
```

Long story short, try executing <code>use_constants.py</code> <b>inside</b> <code>child/</code>.
```
(rlcomp2020-tf2) [phunc20@artichaut-x220 child]$ python use_constants.py
(Before) sys.path = ['/home/phunc20/samsung-SATA/git-repos/github/phunc20/python/import/parent/child', '/home/phunc20/.virtualenvs/rlcomp2020-tf2/lib/python36.zip', '/home/phunc20/.virtualenvs/rlcomp2020-tf2/lib/python3.6',
'/home/phunc20/.virtualenvs/rlcomp2020-tf2/lib/python3.6/lib-dynload', '/usr/lib64/python3.6', '/usr/lib/python3.6', '/home/phunc20/.virtualenvs/rlcomp2020-tf2/lib/python3.6/site-packages']

(After) sys.path = ['/home/phunc20/samsung-SATA/git-repos/github/phunc20/python/import/parent/child', '/home/phunc20/.virtualenvs/rlcomp2020-tf2/lib/python36.zip', '/home/phunc20/.virtualenvs/rlcomp2020-tf2/lib/python3.6', '/home/phunc20/.virtualenvs/rlcomp2020-tf2/lib/python3.6/lib-dynload', '/usr/lib64/python3.6', '/usr/lib/python3.6', '/home/phunc20/.virtualenvs/rlcomp2020-tf2/lib/python3.6/site-packages', '/home/phunc20/samsung-SATA/git-repos/github/phunc20/python/import/parent']

constants.width = 21
```

To understand how all these work, read <b>carefully</b> <code>use_constants.py</code> and also [this stackoverflow post](https://stackoverflow.com/questions/8951255/import-script-from-a-parent-directory/8951269).

