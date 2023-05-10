`np.nextafter` can be used to find the next (or the previous) floating-point number of some float.

Note that we do not have ~`np.prevbefore`~; instead, `np.nextafter` accepts two position args:
`np.nextafter(a, b)`
1. The number `a` whose number we'd like to find out
2. The **direction**; more precisely, the number `b` towards which we'd like to find `a`'s next number

```python
In [13]: np.nextafter(1, 2, dtype=np.float32) == np.float32(1) + np.finfo(np.float32).eps
Out[13]: True

In [14]: np.nextafter(1, 0, dtype=np.float32) == np.float32(1) - np.finfo(np.float32).eps/2
Out[14]: True
```
