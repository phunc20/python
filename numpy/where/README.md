`np.where()` returns a tuple of indices where there is `True`.

```python
In [4]: A = np.random.randint(low=-1, high=1, size=(3,3))
   ...: A
Out[4]: 
array([[ 0,  0, -1],
       [-1,  0,  0],
       [-1,  0, -1]])

In [5]: np.where(A != 0)
Out[5]: (array([0, 1, 2, 2]), array([2, 0, 0, 2]))

In [6]: np.where([True, False, True])
Out[6]: (array([0, 2]),)
```
