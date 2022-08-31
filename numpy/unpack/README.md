# Unpacking An Ndarray
One can unpack an ndarray just like unpacking a list.
```python
In [51]: import numpy as np

In [52]: a = np.random.randn(4)

In [53]: a
Out[53]: array([-0.8070825 ,  0.66094345,  0.39322646, -0.81392358])

In [54]: x,y,z,w = a

In [55]: x,y,z,w
Out[55]:
(-0.8070825010276167,
 0.6609434493986881,
 0.3932264625415844,
 -0.8139235847568814)
```


In the above case, the shape of the ndarray is `(k,)`. When the dimension
of the ndarray is not `1`, one has to make sure the first dimension has the
same number as the number of unpacked elements.
```python
In [56]: x,y,z,w = a.reshape((1,4))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [56], in <cell line: 1>()
----> 1 x,y,z,w = a.reshape((1,4))

ValueError: not enough values to unpack (expected 4, got 1)

In [57]: x,y,z,w = a.reshape((4,1))

In [58]: x,y,z,w
Out[58]:
(array([-0.8070825]),
 array([0.66094345]),
 array([0.39322646]),
 array([-0.81392358]))
```
