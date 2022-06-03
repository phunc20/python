from numba import jit
import numpy as np
from scipy.spatial import distance_matrix


def dist_mx(y0s, y1s):
    row = y0s.reshape((1,-1))
    col = y1s.reshape((-1,1))
    return np.abs(row-col)


@jit(nopython=True)
def jitted_dist_mx(y0s, y1s):
    row = y0s.reshape((1,-1))
    col = y1s.reshape((-1,1))
    return np.abs(row-col)

%%timeit
n_rows = np.random.randint(low=3, high=20)
n_cols = np.random.randint(low=3, high=20)
y0s = np.random.randint(low=0, high=1024, size=(n_rows,))
y1s = np.random.randint(low=0, high=1024, size=(n_cols,))
jitted_dist_mx(y0s, y1s)

"""
In [10]: %timeit jitted_dist_mx(y0s, y1s)
1.05 µs ± 7.01 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [11]: %timeit dist_mx(y0s, y1s)
2.28 µs ± 11.8 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [15]: %%timeit
    ...: n_rows = np.random.randint(low=3, high=20)
    ...: n_cols = np.random.randint(low=3, high=20)
    ...: y0s = np.random.randint(low=0, high=1024, size=(n_rows,))
    ...: y1s = np.random.randint(low=0, high=1024, size=(n_cols,))
    ...: jitted_dist_mx(y0s, y1s)
    ...:
    ...:
28.3 µs ± 1.96 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [16]: %%timeit
    ...: n_rows = np.random.randint(low=3, high=20)
    ...: n_cols = np.random.randint(low=3, high=20)
    ...: y0s = np.random.randint(low=0, high=1024, size=(n_rows,))
    ...: y1s = np.random.randint(low=0, high=1024, size=(n_cols,))
    ...: dist_mx(y0s, y1s)
    ...:
    ...:
33.9 µs ± 3.64 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

"""

%%timeit
n_rows = np.random.randint(low=3, high=20)
n_cols = np.random.randint(low=3, high=20)
y0s = np.random.randint(low=0, high=1024, size=(n_rows,1))
y1s = np.random.randint(low=0, high=1024, size=(n_cols,1))
distance_matrix(y0s, y1s)

"""
!!!
In [8]: np.array_equal(distance_matrix(y0s, y1s), dist_mx(y0s, y1s).astype(np.float64))
Out[8]: False

In [9]: np.array_equiv(distance_matrix(y0s, y1s), dist_mx(y0s, y1s).astype(np.float64))
Out[9]: False

In [10]: np.array_equiv(distance_matrix(y0s, y1s), dist_mx(y1s, y0s).astype(np.float64))
Out[10]: True

In [11]: np.array_equal(distance_matrix(y0s, y1s), dist_mx(y1s, y0s).astype(np.float64))
Out[11]: True

In [26]: %timeit distance_matrix(y0s, y1s)
11.8 µs ± 92.7 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [27]: %timeit distance_matrix(y0s, y1s, p=1)
10.6 µs ± 36.4 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [28]: %timeit dist_mx(y0s, y1s)
2.16 µs ± 8.14 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [29]: %timeit jitted_dist_mx(y0s, y1s)
998 ns ± 8.23 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [30]: %%timeit
    ...: n_rows = np.random.randint(low=3, high=20)
    ...: n_cols = np.random.randint(low=3, high=20)
    ...: y0s = np.random.randint(low=0, high=1024, size=(n_rows,1))
    ...: y1s = np.random.randint(low=0, high=1024, size=(n_cols,1))
    ...: distance_matrix(y0s, y1s)
    ...:
    ...:
45.5 µs ± 88.7 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [31]: %%timeit
    ...: n_rows = np.random.randint(low=3, high=20)
    ...: n_cols = np.random.randint(low=3, high=20)
    ...: y0s = np.random.randint(low=0, high=1024, size=(n_rows,1))
    ...: y1s = np.random.randint(low=0, high=1024, size=(n_cols,1))
    ...: jitted_dist_mx(y0s, y1s)
    ...:
    ...:
28 µs ± 1.32 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [32]: %%timeit
    ...: n_rows = np.random.randint(low=3, high=20)
    ...: n_cols = np.random.randint(low=3, high=20)
    ...: y0s = np.random.randint(low=0, high=1024, size=(n_rows,1))
    ...: y1s = np.random.randint(low=0, high=1024, size=(n_cols,1))
    ...: dist_mx(y0s, y1s)
    ...:
    ...:
29.3 µs ± 61.5 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [33]: %%timeit
    ...: n_rows = np.random.randint(low=3, high=20)
    ...: n_cols = np.random.randint(low=3, high=20)
    ...: y0s = np.random.randint(low=0, high=1024, size=(n_rows,1))
    ...: y1s = np.random.randint(low=0, high=1024, size=(n_cols,1))
    ...: distance_matrix(y0s, y1s, p=1)
    ...:
    ...:
43.8 µs ± 650 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
"""
