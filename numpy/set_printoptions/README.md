```python
In [60]: np.set_printoptions(precision=2)

In [61]: a = np.random.randn(4)

In [62]: a
Out[62]: array([-0.86, -0.69, -0.34,  0.01])

In [63]: x,y,z,w = a

In [64]: x,y,z,w
Out[64]:
(-0.8070825010276167,
 0.6609434493986881,
 0.3932264625415844,
 -0.8139235847568814)

In [65]: x,y,z,w = a.reshape((4,1))

In [65]: x,y,z,w
Out[65]: (array([-0.81]), array([0.66]), array([0.39]), array([-0.81]))
```
