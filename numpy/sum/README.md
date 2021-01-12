## How to better understand the result of `np.sum(A)` when `A` is an `ndarray`?
The best way I can find to explain this is as follows. Say, `A` is an `ndarray` of
`shape=(a0, a1, a2, a3)`, then `C = np.sum(A, axis=2)` will be another `ndarray` of
`shape=(a0,a1,a3)` such that for all (fixed) `0<=b0<a0, 0<=b1<a1, 0<=b3<a3`, we have
`C[b0,b1,b3] = sum(A[b0,b1,i,b3] for i in range(b2))`.



```python
some_shape = (4,4,3)
np.prod(some_shape)
48


M = np.arange(np.prod(some_shape)).reshape(some_shape)
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11]],

       [[12, 13, 14],
        [15, 16, 17],
        [18, 19, 20],
        [21, 22, 23]],

       [[24, 25, 26],
        [27, 28, 29],
        [30, 31, 32],
        [33, 34, 35]],

       [[36, 37, 38],
        [39, 40, 41],
        [42, 43, 44],
        [45, 46, 47]]])


np.sum(M)
1128


np.sum(M, axis=-1)
array([[  3,  12,  21,  30],
       [ 39,  48,  57,  66],
       [ 75,  84,  93, 102],
       [111, 120, 129, 138]])


M[...,0], M[...,1], M[...,2]
(array([[ 0,  3,  6,  9],
        [12, 15, 18, 21],
        [24, 27, 30, 33],
        [36, 39, 42, 45]]),
 array([[ 1,  4,  7, 10],
        [13, 16, 19, 22],
        [25, 28, 31, 34],
        [37, 40, 43, 46]]),
 array([[ 2,  5,  8, 11],
        [14, 17, 20, 23],
        [26, 29, 32, 35],
        [38, 41, 44, 47]]))

```
