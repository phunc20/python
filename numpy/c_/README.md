## `np.c_[]`
This is a convenient way to construct matrices with known columns.

For example,
```python
In [1]: np.c_[[1,2,3], [4,5,6]]
Out[1]:
array([[1, 4],
       [2, 5],
       [3, 6]])

In [2]: np.c_[[1,2,3], [4,5,6]].dtype
Out[2]: dtype('int32')

In [3]: np.c_[[[1,2,3]], [[4,5,6]]]
Out[3]: array([[1, 2, 3, 4, 5, 6]])

In [4]: np.c_[[[1,2,3]], 0, 0, [[4,5,6]]]
Out[4]: array([[1, 2, 3, 0, 0, 4, 5, 6]])

In [5]: np.c_[np.ones((4,1)), np.zeros((4,1))]
Out[5]:
array([[1., 0.],
       [1., 0.],
       [1., 0.],
       [1., 0.]])

In [6]: np.c_[np.ones((3,1)), np.zeros((4,1))]
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-10-bc15c77efcb0> in <module>
----> 1 np.c_[np.ones((3,1)), np.zeros((4,1))]

~/.virtualenvs/py3.7/lib/python3.7/site-packages/numpy/lib/index_tricks.py in __getitem__(self, key)
    404                 objs[k] = objs[k].astype(final_dtype)
    405
--> 406         res = self.concatenate(tuple(objs), axis=axis)
    407
    408         if matrix:

<__array_function__ internals> in concatenate(*args, **kwargs)

ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 3 and the array at index 1 has size 4
```
