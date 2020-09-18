## Syntax
<code><b>np.append(array1, array2)</b></code>

```python
In [73]: np.random.choice(range(6,13), size=3, replace=False)
Out[73]: array([ 7,  6, 10])

In [74]: np.random.choice(range(6,13), size=3, replace=False)
Out[74]: array([10,  8,  9])

In [75]: np.random.choice(range(6,13), size=3, replace=False)
Out[75]: array([ 8, 10, 11])

In [76]: np.random.choice(range(6,13), size=3, replace=False)
Out[76]: array([10,  6,  9])

In [84]: two = np.random.choice(range(6), size=2, replace=False)

In [85]: two
Out[85]: array([1, 3])

In [86]: two = np.random.choice(range(6), size=2, replace=False)

In [88]: two
Out[88]: array([2, 1])

In [89]: two = np.random.choice(range(6), size=2, replace=False)

In [90]: two
Out[90]: array([4, 2])

In [91]: two = np.random.choice(range(6), size=2, replace=False)
    ...: three = np.random.choice(range(6, 13), size=3, replace=False)
    ...: five = np.append(two, three)
    ...:

In [92]: five
Out[92]: array([4, 1, 7, 9, 8])

```


**Rmk.** Note that more than 2 input arg of arrays is not allowed:
```python
In [94]: np.append([1,2], [3,4], [5,6,7])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-94-399611584f52> in <module>
----> 1 np.append([1,2], [3,4], [5,6,7])

<__array_function__ internals> in append(*args, **kwargs)

~/.virtualenvs/rlcomp2020-tf2.2.0/lib/python3.6/site-packages/numpy/lib/function_base.py in append(arr, values, axis)
   4669         values = ravel(values)
   4670         axis = arr.ndim-1
-> 4671     return concatenate((arr, values), axis=axis)
   4672
   4673

<__array_function__ internals> in concatenate(*args, **kwargs)

TypeError: 'list' object cannot be interpreted as an integer

In [95]: np.append([1,2], [3,4])
Out[95]: array([1, 2, 3, 4])
```
