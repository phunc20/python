Like `sorted()`, `min()` and `max()` also have a `key=func` key-value
argument to enable a more customized functionality.

```python
In [1]: min?
Docstring:
min(iterable, *[, default=obj, key=func]) -> value
min(arg1, arg2, *args, *[, key=func]) -> value

With a single iterable argument, return its smallest item. The
default keyword-only argument specifies an object to return if
the provided iterable is empty.
With two or more arguments, return the smallest argument.
Type:      builtin_function_or_method

In [2]: L = [
   ...:   {"x": 10, "y": 20},
   ...:   {"x": 30, "y": 18},
   ...:   {"x": 31, "y": 40},
   ...:   {"x":  9, "y": 39},]

In [3]: min(L, key=lambda D: D["x"] + D["y"])
Out[3]: {'x': 10, 'y': 20}
```
