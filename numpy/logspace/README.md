According to the doc, `np.logspace`
> Return numbers spaced evenly on a log scale.

More concretly, what `np.logspace(start, stop, num=k, base=b)` does
is `base**(np.linspace(start, stop, num=k))`, i.e.
1. We first sapce evenly points on the interval $[\texttt{start}, \texttt{stop}]$
1. Then we raise these evenly spaced points to the exponential of `base=b`

```python
In [2]: np.logspace(0,2,num=5)
Out[2]:
array([  1.        ,   3.16227766,  10.        ,  31.6227766 ,
       100.        ])

In [3]: np.array_equal(10**np.linspace(0,2,num=5), np.logspace(0,2,num=5))
Out[3]: True

In [4]: np.array_equal(10**np.linspace(0,2,num=5,endpoint=False), np.logspace(0,2,num=5,endpoint=False))
Out[4]: True
```
