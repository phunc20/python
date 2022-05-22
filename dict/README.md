## Test Key Existence
Use `k in D` instead of `k in D.keys()`.
```python
In [1]: D = dict(zip("abc", range(3))); D
Out[1]: {'a': 0, 'b': 1, 'c': 2}

In [2]: %timeit "a" in D
39.5 ns ± 4.3 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

In [3]: %timeit "a" in D.keys()
93.4 ns ± 0.732 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

In [4]: %timeit "z" in D
41.5 ns ± 4.12 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

In [5]: %timeit "z" in D.keys()
95.9 ns ± 7.17 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
```


## As A Data Structure for Storing Images
From MIT's 6.006 course, I realized that we can actually use the Python dictionary
as a means to store image data:

```python
In [1]: D = dict()

In [2]: D[0, 0] = 255

In [3]: D[0, 1] = 120

In [4]: D
Out[4]: {(0, 0): 255, (0, 1): 120}

In [5]:
```

To put in simpler terms, the assignment `D[0, 0] = 255` is not diff from
`D[(0, 0)] = 255`






