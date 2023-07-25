## Input Args
- `endpoint`.  
  Let's start our explanation of the difference btw
  `endpoint=True` and `endpoint=False` by an example:
  ```python
  In [2]: np.linspace(0,1,num=10,endpoint=True)
  Out[2]:
  array([0.        , 0.11111111, 0.22222222, 0.33333333, 0.44444444,
         0.55555556, 0.66666667, 0.77777778, 0.88888889, 1.        ])
  
  In [3]: np.linspace(0,1,num=10,endpoint=False)
  Out[3]: array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
  ```
  We can notice that
      1. Both of the results above are of length `10` as demanded by `num=10`
  
  It's easier to understand `Out[2]`: It needs to include the endpoint `1`,
  so the 10 points must divide the entire interval $[0,1]$ into `9` equal
  subintervals  
  As for `Out[3]`, why
      1. The array ends at `0.9`?
      1. The step seems to be `0.1`?
  
  The doc doesn't make it too clear as to how it is done, but I have found
  a plausible explanation: `np.linspace(a,b,num=k,endpoint=False)`
  simply divides the interval $[a, b]$ into `k` subintervals (instead of
  `k-1` subintervals in the case of `endpoint=True`), then the output is then
  simply $[a, a+\frac{b-a}{k}, \ldots, a+(k-1)\frac{b-a}{k}]$.
