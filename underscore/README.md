## `_`
We often see `_` in a for loop where we do not really care about the elements we loop through, e.g.
```python
for _ in range(100):
    <do_sth>
```
In fact, `_` is just a variable name like any other variable names like `i, n, a, b, c`, etc.
```python
In [1]: _ = "abc"

In [2]: _
Out[2]: 'abc'

In [3]: _ = 17

In [4]: _
Out[4]: 17

In [5]: for _ in range(10):
   ...:     pass
   ...:

In [6]: _
Out[6]: 9
```
