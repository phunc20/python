A good example is worth sometimes more than a thousand words.

**Note.** The `axis=` arg can be any integer from
`0` to `X.ndim` (in this case `2`), whereas the axis
of `X` itself only goes from `0` to `X.ndim-1`.

```ipython
In [1]: import numpy as np

In [2]: X = np.random.rand(7, 3)
   ...: X.shape
Out[2]: (7, 3)

In [3]: XX = np.expand_dims(X, axis=0)
   ...: XX.shape
Out[3]: (1, 7, 3)

In [4]: XX = np.expand_dims(X, axis=1)
   ...: XX.shape
Out[4]: (7, 1, 3)

In [5]: XX = np.expand_dims(X, axis=2)
   ...: XX.shape
Out[5]: (7, 3, 1)

In [6]: XX = np.expand_dims(X, axis=3)
   ...: XX.shape
AxisError: axis 3 is out of bounds for array of dimension 3

In [7]: XX = np.expand_dims(X, axis=-1)
   ...: XX.shape
Out[7]: (7, 3, 1)

In [8]:
```
