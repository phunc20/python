```python
In [1]: a = None

In [2]: NoneType = type(None)

In [3]: isinstance(a, NoneType)
Out[3]: True

In [4]: %timeit isinstance(a, NoneType)
65.6 ns ± 4.13 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

In [5]: %timeit a is None
37.6 ns ± 1.18 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

In [6]: b = NoneType()

In [7]: id(a) == id(b)
Out[7]: True

In [8]: id(a) == id(None)
Out[8]: True

In [9]: c = NoneType()

In [10]: id(c) == id(None)
Out[10]: True

In [11]: def function_that_does_nothing(): pass

In [12]: e = function_that_does_nothing()

In [13]: id(e) == id(None)
Out[13]: True
```

Cf. <https://stackoverflow.com/questions/3289601/null-object-in-python/48504780#48504780>
