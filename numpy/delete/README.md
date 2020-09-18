## How is roughly how to use <code>np.delete()</code>
<code>np.delete()</code> will return a new ndarray, instead of modifying its input in place.

```python
K = np.array([
       [0, 1],
       [2, 3],
       [4, 5],
       [6, 7]])

In [55]: np.delete(K, -1, axis=0)
Out[55]:
array([[0, 1],
       [2, 3],
       [4, 5]])

In [56]: np.delete(K, 1, axis=0)
Out[56]:
array([[0, 1],
       [4, 5],
       [6, 7]])

In [62]: np.delete(K, [], axis=0)
Out[62]:
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7]])
```
