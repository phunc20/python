
In [1]: %timeit d = {}
52.3 ns ± 0.132 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

In [2]: %timeit d = dict()
156 ns ± 0.322 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

In [3]: type({})
Out[3]: dict

In [4]: %timeit l = []
51.4 ns ± 0.0464 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

In [5]: %timeit l = list()
145 ns ± 0.0895 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

In [6]:
