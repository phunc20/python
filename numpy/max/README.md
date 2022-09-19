It seems less recommended to use `max()` on an ndarray in order to find the maximum. Indeed,
```python
In [1]: import numpy as np

In [2]: a = np.random.randint(low=0, high=30_000, size=(5000,))

In [3]: %timeit a.max()
4.29 µs ± 7.31 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [4]: %timeit np.max(a)
5.87 µs ± 25.9 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [5]: %timeit max(a)
256 µs ± 352 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```
