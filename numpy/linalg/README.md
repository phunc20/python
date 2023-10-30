## SVD
```python
In [1]: import numpy as np

In [2]: m, n = 2, 3

In [3]: np.random.seed(42)

In [4]: A = np.random.rand(m, n)

In [5]: U, S, V = np.linalg.svd(A)

In [6]: print(f'{U.shape = }')
U.shape = (2, 2)

In [7]: print(f'{V.shape = }')
V.shape = (3, 3)

In [8]: print(f'{S.shape = }')
S.shape = (2,)

In [10]: S
Out[10]: array([1.32500252, 0.48102966])

In [35]: np.linalg.norm(U @ U.T - np.eye(U.shape[0]))
Out[35]: 7.468566216113836e-16

In [36]: np.linalg.norm(V @ V.T - np.eye(V.shape[0]))
Out[36]: 1.0574576753951156e-15

In [37]: Sigma = np.zeros((m, n))

In [38]: Sigma.dtype
Out[38]: dtype('float64')

In [39]: U.dtype
Out[39]: dtype('float64')

In [40]: for i, s in enumerate(S):
    ...:     Sigma[i, i] = s
    ...:

In [41]: Sigma
Out[41]:
array([[1.32500252, 0.        , 0.        ],
       [0.        , 0.48102966, 0.        ]])

In [42]: np.allclose(A, U @ Sigma @ V)
Out[42]: True
```
