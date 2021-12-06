- used to construct lists, e.g.
  ```python
  In [1]: L = [i for i in range(5)]
  
  In [2]: L2 = [*L, 5]
  
  In [3]: L2
  Out[3]: [0, 1, 2, 3, 4, 5]
  
  In [4]: [*L, *range(5,10)]
  Out[4]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```











