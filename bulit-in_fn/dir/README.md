# `dir()`
`dir(obj)` will return the methods, attributes, etc. of the object `obj` as a list of strings.

The following convenience function might prove to be useful sometimes.

```python
def non_dunder(obj):
    return [s for s in dir(obj) if not s.startswith("__")]

```
