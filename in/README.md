## Efficiency
Constructing a `dict` is more time-consuming than constructing a `list`
```python
In [35]: %timeit {chr(i): i for i in range(100)}
8.79 µs ± 30 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [36]: %timeit [chr(i) for i in range(100)]
5.89 µs ± 25.8 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

But once constructed, testing whether sth is `in` a `dict` is faster:
```python
In [26]: L = [chr(i) for i in range(100)]

In [27]: D = {chr(i): i for i in range(100)}

In [28]: %timeit chr(0) in L
70.3 ns ± 0.0807 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [29]: %timeit chr(0) in D
72.9 ns ± 0.142 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [30]: %timeit chr(200) in D
71.9 ns ± 0.191 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [31]: %timeit chr(200) in L
1.46 µs ± 2.08 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [32]: %timeit chr(100) in L
1.46 µs ± 5.86 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [33]: %timeit chr(100) in D
73 ns ± 1.31 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

Testing `in` a `list` seems to be a simple `for` loop test, so when the element in question
lies around the end of a long list, it could take long to test `in`. And when the element
does not exist in the list, Python will have to run through the entire list to test `in`.

