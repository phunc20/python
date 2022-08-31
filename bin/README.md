```python
In [18]: bin(156)
Out[18]: '0b10011100'

In [19]: int(bin(156), 2)
Out[19]: 156

In [21]: a = 156

In [22]: %timeit f"{a:b}"
372 ns ± 2.9 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [23]: f"{a:b}"
    ...:
Out[23]: '10011100'

In [24]: int(f"{a:b}", 2)
Out[24]: 156

In [25]: %timeit bin(a)
203 ns ± 1.9 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [26]: bin(a)
Out[26]: '0b10011100'
```
