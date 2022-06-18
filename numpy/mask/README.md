
- Use a mask to remove an entry from a fixed axis.
```python
In [46]: shape = (512, 6); A = np.random.randint(0, 100, size=shape)

In [47]: A
Out[47]:
array([[45, 67, 17, 32, 68, 73],
       [99, 65, 41, 72,  0,  3],
       [14, 58, 39, 56,  5, 41],
       ...,
       [39, 95, 33, 41, 35, 56],
       [37, 82, 57, 27, 56, 50],
       [ 6, 93, 69, 30, 47, 99]])

In [48]: mask = np.ones(shape, dtype=bool)

In [49]: mask
Out[49]:
array([[ True,  True,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True,  True],
       ...,
       [ True,  True,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True,  True]])

In [50]: mask.shape
Out[50]: (512, 6)

In [51]: A[mask]
Out[51]: array([45, 67, 17, ..., 30, 47, 99])

In [52]: A[mask].shape
Out[52]: (3072,)

In [53]: np.array_equal(A[mask].reshape(shape), A)
Out[53]: True

In [54]: A[[3,4], [0,-1]]
Out[54]: array([52, 13])

In [55]: A
Out[55]:
array([[45, 67, 17, 32, 68, 73],
       [99, 65, 41, 72,  0,  3],
       [14, 58, 39, 56,  5, 41],
       ...,
       [39, 95, 33, 41, 35, 56],
       [37, 82, 57, 27, 56, 50],
       [ 6, 93, 69, 30, 47, 99]])

In [56]: A[[0,1], [0,-1]]
Out[56]: array([45,  3])

In [57]: A[[0,1], [0,-1]] = -300

In [58]: A
Out[58]:
array([[-300,   67,   17,   32,   68,   73],
       [  99,   65,   41,   72,    0, -300],
       [  14,   58,   39,   56,    5,   41],
       ...,
       [  39,   95,   33,   41,   35,   56],
       [  37,   82,   57,   27,   56,   50],
       [   6,   93,   69,   30,   47,   99]])

In [59]: argmax_indices = np.argmax(A, axis=-1); argmax_indices
Out[59]:
array([5, 0, 1, 1, 4, 1, 4, 4, 1, 4, 4, 3, 2, 5, 4, 1, 3, 5, 2, 4, 0, 0,
       2, 3, 0, 3, 0, 0, 5, 1, 1, 0, 0, 3, 0, 3, 1, 0, 1, 2, 3, 0, 5, 4,
       0, 3, 1, 3, 0, 5, 3, 0, 1, 4, 5, 0, 2, 2, 5, 3, 4, 0, 1, 5, 0, 1,
       5, 0, 1, 5, 4, 2, 2, 4, 5, 2, 2, 0, 2, 0, 0, 5, 2, 5, 0, 1, 4, 0,
       2, 5, 1, 0, 1, 3, 2, 0, 3, 5, 2, 4, 3, 0, 2, 1, 0, 5, 4, 1, 5, 0,
       1, 5, 5, 0, 5, 2, 4, 5, 2, 5, 1, 4, 3, 3, 5, 3, 0, 2, 0, 2, 2, 2,
       2, 4, 4, 2, 0, 2, 0, 3, 4, 5, 5, 3, 5, 4, 0, 1, 0, 1, 4, 5, 3, 3,
       5, 2, 3, 4, 0, 4, 3, 2, 0, 3, 3, 2, 3, 0, 4, 3, 5, 1, 2, 0, 4, 0,
       1, 1, 3, 0, 1, 0, 4, 3, 1, 1, 1, 0, 0, 2, 5, 1, 4, 3, 0, 1, 1, 3,
       0, 5, 4, 4, 3, 5, 2, 4, 5, 3, 4, 0, 2, 4, 1, 4, 2, 1, 5, 1, 2, 3,
       0, 2, 0, 2, 4, 4, 2, 3, 2, 0, 3, 0, 4, 5, 3, 1, 0, 5, 0, 2, 4, 0,
       4, 2, 0, 1, 0, 5, 3, 2, 3, 5, 0, 1, 3, 1, 4, 2, 4, 2, 4, 0, 2, 2,
       0, 0, 3, 5, 2, 4, 4, 5, 4, 3, 2, 3, 4, 3, 3, 2, 0, 5, 5, 5, 4, 1,
       2, 5, 0, 4, 3, 0, 5, 5, 0, 4, 3, 1, 3, 1, 4, 3, 1, 4, 5, 0, 2, 0,
       3, 2, 5, 5, 5, 4, 0, 5, 2, 0, 1, 0, 0, 4, 1, 1, 0, 4, 5, 4, 1, 0,
       2, 0, 0, 3, 5, 1, 4, 2, 4, 3, 0, 1, 2, 0, 2, 5, 4, 1, 5, 0, 3, 0,
       5, 0, 1, 3, 0, 4, 2, 0, 3, 5, 3, 0, 5, 4, 5, 0, 2, 0, 5, 0, 5, 3,
       3, 3, 4, 3, 1, 2, 1, 1, 2, 3, 0, 0, 4, 2, 3, 4, 4, 3, 2, 3, 4, 2,
       1, 5, 2, 0, 4, 3, 1, 3, 5, 3, 4, 1, 5, 3, 1, 3, 3, 3, 2, 5, 0, 3,
       4, 5, 5, 5, 4, 0, 0, 2, 1, 3, 3, 2, 3, 0, 1, 1, 1, 1, 2, 1, 4, 5,
       3, 1, 2, 2, 4, 3, 0, 1, 3, 1, 2, 3, 3, 5, 0, 2, 5, 0, 2, 4, 4, 5,
       4, 3, 5, 5, 2, 3, 4, 3, 1, 3, 1, 1, 2, 0, 0, 1, 0, 3, 4, 3, 0, 0,
       0, 5, 5, 3, 4, 0, 2, 1, 3, 2, 5, 5, 1, 5, 5, 2, 2, 3, 2, 5, 1, 1,
       1, 4, 4, 1, 1, 5])

In [60]: mask.shape
Out[60]: (512, 6)

In [62]: mask[range(A.shape[0]), argmax_indices] = False

In [63]: mask
Out[63]:
array([[ True,  True,  True,  True,  True, False],
       [False,  True,  True,  True,  True,  True],
       [ True, False,  True,  True,  True,  True],
       ...,
       [ True, False,  True,  True,  True,  True],
       [ True, False,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True, False]])

In [64]: argmax_indices
Out[64]:
array([5, 0, 1, 1, 4, 1, 4, 4, 1, 4, 4, 3, 2, 5, 4, 1, 3, 5, 2, 4, 0, 0,
       2, 3, 0, 3, 0, 0, 5, 1, 1, 0, 0, 3, 0, 3, 1, 0, 1, 2, 3, 0, 5, 4,
       0, 3, 1, 3, 0, 5, 3, 0, 1, 4, 5, 0, 2, 2, 5, 3, 4, 0, 1, 5, 0, 1,
       5, 0, 1, 5, 4, 2, 2, 4, 5, 2, 2, 0, 2, 0, 0, 5, 2, 5, 0, 1, 4, 0,
       2, 5, 1, 0, 1, 3, 2, 0, 3, 5, 2, 4, 3, 0, 2, 1, 0, 5, 4, 1, 5, 0,
       1, 5, 5, 0, 5, 2, 4, 5, 2, 5, 1, 4, 3, 3, 5, 3, 0, 2, 0, 2, 2, 2,
       2, 4, 4, 2, 0, 2, 0, 3, 4, 5, 5, 3, 5, 4, 0, 1, 0, 1, 4, 5, 3, 3,
       5, 2, 3, 4, 0, 4, 3, 2, 0, 3, 3, 2, 3, 0, 4, 3, 5, 1, 2, 0, 4, 0,
       1, 1, 3, 0, 1, 0, 4, 3, 1, 1, 1, 0, 0, 2, 5, 1, 4, 3, 0, 1, 1, 3,
       0, 5, 4, 4, 3, 5, 2, 4, 5, 3, 4, 0, 2, 4, 1, 4, 2, 1, 5, 1, 2, 3,
       0, 2, 0, 2, 4, 4, 2, 3, 2, 0, 3, 0, 4, 5, 3, 1, 0, 5, 0, 2, 4, 0,
       4, 2, 0, 1, 0, 5, 3, 2, 3, 5, 0, 1, 3, 1, 4, 2, 4, 2, 4, 0, 2, 2,
       0, 0, 3, 5, 2, 4, 4, 5, 4, 3, 2, 3, 4, 3, 3, 2, 0, 5, 5, 5, 4, 1,
       2, 5, 0, 4, 3, 0, 5, 5, 0, 4, 3, 1, 3, 1, 4, 3, 1, 4, 5, 0, 2, 0,
       3, 2, 5, 5, 5, 4, 0, 5, 2, 0, 1, 0, 0, 4, 1, 1, 0, 4, 5, 4, 1, 0,
       2, 0, 0, 3, 5, 1, 4, 2, 4, 3, 0, 1, 2, 0, 2, 5, 4, 1, 5, 0, 3, 0,
       5, 0, 1, 3, 0, 4, 2, 0, 3, 5, 3, 0, 5, 4, 5, 0, 2, 0, 5, 0, 5, 3,
       3, 3, 4, 3, 1, 2, 1, 1, 2, 3, 0, 0, 4, 2, 3, 4, 4, 3, 2, 3, 4, 2,
       1, 5, 2, 0, 4, 3, 1, 3, 5, 3, 4, 1, 5, 3, 1, 3, 3, 3, 2, 5, 0, 3,
       4, 5, 5, 5, 4, 0, 0, 2, 1, 3, 3, 2, 3, 0, 1, 1, 1, 1, 2, 1, 4, 5,
       3, 1, 2, 2, 4, 3, 0, 1, 3, 1, 2, 3, 3, 5, 0, 2, 5, 0, 2, 4, 4, 5,
       4, 3, 5, 5, 2, 3, 4, 3, 1, 3, 1, 1, 2, 0, 0, 1, 0, 3, 4, 3, 0, 0,
       0, 5, 5, 3, 4, 0, 2, 1, 3, 2, 5, 5, 1, 5, 5, 2, 2, 3, 2, 5, 1, 1,
       1, 4, 4, 1, 1, 5])


In [66]: A2 = A[mask].reshape(shape[0], shape[1]-1); A2.shape, A.shape
Out[66]: ((512, 5), (512, 6))

In [67]: A2
Out[67]:
array([[-300,   67,   17,   32,   68],
       [  65,   41,   72,    0, -300],
       [  14,   39,   56,    5,   41],
       ...,
       [  39,   33,   41,   35,   56],
       [  37,   57,   27,   56,   50],
       [   6,   93,   69,   30,   47]])

In [68]: A
Out[68]:
array([[-300,   67,   17,   32,   68,   73],
       [  99,   65,   41,   72,    0, -300],
       [  14,   58,   39,   56,    5,   41],
       ...,
       [  39,   95,   33,   41,   35,   56],
       [  37,   82,   57,   27,   56,   50],
       [   6,   93,   69,   30,   47,   99]])





```



### Complexity
It seems that manually finding the 2nd argmax has a smaller
time complexity than `argsort()` the whole array, but
the constant multiplied to the manually finding is big,
so when the array `A` is small, it's actually more
time-consuming to do the manual one than `argsort()`:
```python
In [111]: shape = (512, 7)
     ...: randint_low = 0
     ...: # should be high enought, otherwise max2_indices and
     ...: # m2_ind may not equal in the following: There exist
     ...: # more than one way to sort an array with repeated numbers.
     ...: randint_high = randint_low + 1_000_000
     ...: A = np.random.randint(randint_low, randint_high, size=shape)

In [112]: %%timeit
     ...: sorted_indices = np.argsort(A, axis=-1)
     ...: m2_ind = sorted_indices[..., -2]
     ...: m_ind = sorted_indices[..., -1]
     ...:
     ...:
31.5 µs ± 50.5 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [113]: %%timeit
     ...: max_indices = np.argmax(A, axis=-1)
     ...: mask = np.ones(shape, dtype=bool)
     ...: mask[range(A.shape[0]), max_indices] = False
     ...: A2 = A[mask].reshape(shape[0], shape[1]-1)
     ...: tmp_max2_indices = np.argmax(A2, axis=-1)
     ...: max2_indices = tmp_max2_indices + (tmp_max2_indices >= max_indices)
     ...:
     ...:
74.1 µs ± 314 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [106]: shape = (512, 17)
     ...: randint_low = 0
     ...: # should be high enought, otherwise max2_indices and
     ...: # m2_ind may not equal in the following: There exist
     ...: # more than one way to sort an array with repeated numbers.
     ...: randint_high = randint_low + 1_000_000
     ...: A = np.random.randint(randint_low, randint_high, size=shape)
     ...:

In [107]: %%timeit
     ...: sorted_indices = np.argsort(A, axis=-1)
     ...: m2_ind = sorted_indices[..., -2]
     ...: m_ind = sorted_indices[..., -1]
     ...:
     ...:
132 µs ± 515 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [108]: %%timeit
     ...: max_indices = np.argmax(A, axis=-1)
     ...: mask = np.ones(shape, dtype=bool)
     ...: mask[range(A.shape[0]), max_indices] = False
     ...: A2 = A[mask].reshape(shape[0], shape[1]-1)
     ...: tmp_max2_indices = np.argmax(A2, axis=-1)
     ...: max2_indices = tmp_max2_indices + (tmp_max2_indices >= max_indices)
     ...:
     ...:
100 µs ± 472 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
```
More extremely,
```python

In [3]: # -----------------------------
   ...: #  TEST COMPLEXITY / EXE TIME
   ...: # -----------------------------
   ...: shape = (512, 100)
   ...: #shape = (512, 17)
   ...: randint_low = 0
   ...: randint_high = randint_low + 1_000_000
   ...: A = np.random.randint(randint_low, randint_high, size=shape)
   ...:

In [4]: %%timeit
   ...: max_indices = np.argmax(A, axis=-1)
   ...: mask = np.ones(shape, dtype=bool)
   ...: mask[range(A.shape[0]), max_indices] = False
   ...: A2 = A[mask].reshape(shape[0], shape[1]-1)
   ...: tmp_max2_indices = np.argmax(A2, axis=-1)
   ...: max2_indices = tmp_max2_indices + (tmp_max2_indices >= max_indices)
   ...:
   ...:
203 µs ± 1.18 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

In [5]: %%timeit
   ...: sorted_indices = np.argsort(A, axis=-1)
   ...: m2_ind = sorted_indices[..., -2]
   ...: m_ind = sorted_indices[..., -1]
   ...:
   ...:
1.29 ms ± 5.38 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

In [15]: # -----------------------------
    ...: #  TEST COMPLEXITY / EXE TIME
    ...: # -----------------------------
    ...: shape = (512, 15)
    ...: randint_low = 0
    ...: randint_high = randint_low + 1_000_000
    ...: A = np.random.randint(randint_low, randint_high, size=shape)

In [16]: %%timeit
    ...: max_indices = np.argmax(A, axis=-1)
    ...: mask = np.ones(shape, dtype=bool)
    ...: mask[range(A.shape[0]), max_indices] = False
    ...: A2 = A[mask].reshape(shape[0], shape[1]-1)
    ...: tmp_max2_indices = np.argmax(A2, axis=-1)
    ...: max2_indices = tmp_max2_indices + (tmp_max2_indices >= max_indices)
    ...:
    ...:

94.6 µs ± 518 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [17]:

In [17]: %%timeit
    ...: sorted_indices = np.argsort(A, axis=-1)
    ...: m2_ind = sorted_indices[..., -2]
    ...: m_ind = sorted_indices[..., -1]
    ...:
    ...:
97.6 µs ± 144 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [18]: %%timeit
    ...: sorted_indices = np.argsort(A, axis=-1)
    ...: m2_ind = sorted_indices[..., -2]
    ...: m_ind = sorted_indices[..., -1]
```


