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

In [9]: s1 = 'a'
   ...: s2 = 'ab'
   ...: s3 = 'abc'
   ...: s4 = 'abcd'
   ...:
   ...: print(f'{s1:<10}_')
   ...: print(f'{s2:<10}_')
   ...: print(f'{s3:<10}_')
   ...: print(f'{s4:<10}_')
a         _
ab        _
abc       _
abcd      _

In [10]: s1 = 'a'
    ...: s2 = 'ab'
    ...: s3 = 'abc'
    ...: s4 = 'abcd'
    ...:
    ...: print(f'{s1:>10}')
    ...: print(f'{s2:>10}')
    ...: print(f'{s3:>10}')
    ...: print(f'{s4:>10}')
         a
        ab
       abc
      abcd

In [11]: a1 = 1
    ...: a2 = 10
    ...: a3 = 100
    ...: a4 = 1000
    ...:
    ...: print(f'{a1:>10d}')
    ...: print(f'{a2:>10d}')
    ...: print(f'{a3:>10d}')
    ...: print(f'{a4:>10d}')
         1
        10
       100
      1000

In [12]: a1 = 1
    ...: a2 = 10
    ...: a3 = 100
    ...: a4 = 1000
    ...:
    ...: print(f'{a1:<10d}_')
    ...: print(f'{a2:<10d}_')
    ...: print(f'{a3:<10d}_')
    ...: print(f'{a4:<10d}_')
1         _
10        _
100       _
1000      _

In [13]: a1 = 1
    ...: a2 = 10
    ...: a3 = 100
    ...: a4 = 1000
    ...:
    ...: print(f'{a1: 10d}_')
    ...: print(f'{a2: 10d}_')
    ...: print(f'{a3: 10d}_')
    ...: print(f'{a4: 10d}_')
         1_
        10_
       100_
      1000_
```
