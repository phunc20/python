```
In [1]: from compare import *

In [2]: %timeit straight_mean(A)
6.22 ms ± 122 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

In [3]: %timeit unnecessary_mean(A)
7.41 s ± 343 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```
