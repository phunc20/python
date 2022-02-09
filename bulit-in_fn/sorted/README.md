# Sorting
When it comes to sort, Python provides this `sorted()` function.
```python
In [1]: help(sorted)

Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.

In [2]: L = [-10, -11, 200]

In [3]: sorted(L)
Out[3]: [-11, -10, 200]

In [4]: sorted(L, reverse=True)
Out[4]: [200, -10, -11]

In [5]: %timeit sorted(L, reverse=True)
572 ns ± 19 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [6]: %timeit reversed(sorted(L))
720 ns ± 4.19 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

## `np.argsort()` and Flexibility
Sometimes what you want is the **indices** of the elements in sorted order instead of the elements themselves.
If you are a NumPy user, you'd certainly be familiar with  the convenient `np.argsort()`.
But you really don't need NumPy every time you want this. See below.
```python

In [7]: import numpy as np

In [8]: np.argsort(L)
Out[8]: array([1, 0, 2])

In [9]: sorted(range(len(L)), key=lambda idx: L[idx])
Out[9]: [1, 0, 2]
```
You simply provide to the `sorted()` function

- as first arg, the indices
- as kwarg `key` a function mapping each index to its corresponding value

The `key` kwarg makes `sorted()` flexible.
