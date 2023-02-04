## Format Strings Using `f""`
```python
In [1]: a = 512

In [2]: print(f"{a=}")
a=512

In [3]: print(f"{a % 7 = }")
a % 7 = 1

In [3]: import random

In [4]: acc = random.random()

In [5]: f"{acc = }"
Out[5]: 'acc = 0.3947075492317721'

In [6]: f"{acc = :.2%}"
Out[6]: 'acc = 39.47%'

In [7]: f"{acc = :.4f}"
Out[7]: 'acc = 0.3947'

In [6]: i = 3000000

In [11]: f"{i = : 10d}"
Out[11]: 'i =    3000000'

In [12]: f"{i = :010d}"
Out[12]: 'i = 0003000000'

In [7]: print(f"{i:05_d}")
3_000_000

In [8]: print(f"{i:05,d}")
3,000,000
```
