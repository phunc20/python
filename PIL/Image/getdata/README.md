Below is an example session of how to use the method `getdata()` of a `PIL.Image`
instance.
```python
In [23]: !python --version
Python 3.7.3

In [24]: from PIL import Image

In [25]: lena = Image.open("../../lena30.jpg")

In [26]: lena.mode
Out[26]: 'RGB'

In [27]: list(lena.getdata())[:10]
Out[27]:
[(226, 136, 127),
 (225, 135, 126),
 (225, 135, 126),
 (225, 135, 126),
 (224, 134, 125),
 (224, 134, 123),
 (224, 134, 123),
 (223, 133, 122),
 (227, 138, 124),
 (226, 137, 123)]

In [28]: import numpy as np

In [30]: w, h = lena.size

In [31]: %timeit array = np.empty((h, w), dtype=np.uint8)
1.1 µs ± 16.1 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [32]: %timeit array = np.zeros((h, w), dtype=np.uint8)
27.6 µs ± 1 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

In [34]: pixels = iter(lena.getdata())

In [38]: next(pixels)
Out[38]: (225, 135, 126)

In [39]: next(pixels)
Out[39]: (224, 134, 125)

In [40]: array = np.empty((h, w, 3), dtype=np.uint8)

In [41]: for i in range(h):
    ...:     for j in range(w):
    ...:         array[i, j] = next(pixels)
    ...:
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-41-257c7d1d47c3> in <module>
      1 for i in range(h):
      2     for j in range(w):
----> 3         array[i, j] = next(pixels)
      4

StopIteration:

In [42]: restored = Image.fromarray(array)

In [43]: restored.show()

In [44]: for i in range(h):
    ...:     for j in range(w):
    ...:         array[i, j] = pixels.next()
    ...:
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-44-685f504eafe9> in <module>
      1 for i in range(h):
      2     for j in range(w):
----> 3         array[i, j] = pixels.next()
      4

AttributeError: 'iterator' object has no attribute 'next'

In [46]: pixels = iter(lena.getdata())

In [47]: for i in range(h):
    ...:     for j in range(w):
    ...:         array[i, j] = next(pixels)
    ...:

In [48]:
```

A few worth noting points are

1. We can use `list()` or `iter()` on the return value of `getdata()`
1. `np.empty()` is faster than `np.zeros()` when what we want is just an randomly initialized array
1. Once you use `next()` on an iterable, it is then one step closer to the end of iteration, which is why we met `StopIteration` the first time and nothing happened the second time when we redid the experiment at the end of the IPython session.
1. We use `restored.show()` to check whether we get the correct image back
1. When `getdata()` becomes an iterable, the order of the pixels are **_column-major_**, i.e. it covers thru the column pixels first.
1. The `.next()` method seems to exist in Python2, but not in Python3.

