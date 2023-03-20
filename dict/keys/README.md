

```python
In [29]: D = dict(zip(range(3), "abc"))

In [30]: D
Out[30]: {0: 'a', 1: 'b', 2: 'c'}

In [31]: type(D.keys())
Out[31]: dict_keys

In [32]: D.keys()[0]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In [32], line 1
----> 1 D.keys()[0]

TypeError: 'dict_keys' object is not subscriptable

In [33]: next(D.keys())
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In [33], line 1
----> 1 next(D.keys())

TypeError: 'dict_keys' object is not an iterator

In [34]: next(iter(D.keys()))
Out[34]: 0

In [35]: %timeit list(D.keys())[0]
502 ns ± 16.6 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [36]: %timeit next(iter(D.keys()))
377 ns ± 2.38 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
```
