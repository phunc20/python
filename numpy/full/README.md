## `np.full()`
can be used to initialize an array full of same value, pretty much like Julia's `fill()` method. Note that it is faster than using `np.ones()` multiplied by that same value.

```python
In [2]: %timeit np.full(shape=(10_000,), fill_value=0.51)
28.5 µs ± 77.6 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

In [3]: %timeit np.ones(shape=(10_000,)) * 0.51
47.2 µs ± 247 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

In [4]: np.array_equal(np.full(shape=(10_000,), fill_value=0.51), np.ones(shape=(10_000,)) * 0.51)
Out[4]: True
```



