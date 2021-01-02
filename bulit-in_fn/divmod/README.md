## `divmod(a, b)` slower than `(a // b, a % b)`?

```python
In [3]: %timeit divmod(17, 7)
177 ns ± 0.776 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [4]: %timeit (17 // 7, 17 % 7)
14 ns ± 2.69 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)

In [5]: %timeit divmod(17, 7)
179 ns ± 1.15 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [6]: %timeit (17 // 7, 17 % 7)
11.6 ns ± 0.0309 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)

In [7]: divmod(17, 7)
Out[7]: (2, 3)

In [8]: %time (17 // 7, 17 % 7)
CPU times: user 5 µs, sys: 0 ns, total: 5 µs
Wall time: 12.9 µs
Out[8]: (2, 3)

In [9]: %time divmod(17, 7)
CPU times: user 7 µs, sys: 0 ns, total: 7 µs
Wall time: 13.4 µs
Out[9]: (2, 3)

In [10]: %time (17 // 7, 17 % 7)
CPU times: user 5 µs, sys: 0 ns, total: 5 µs
Wall time: 12.6 µs
Out[10]: (2, 3)

In [11]: %time divmod(17, 7)
CPU times: user 6 µs, sys: 0 ns, total: 6 µs
Wall time: 14.1 µs
Out[11]: (2, 3)
```
