# `dir()`
`dir(obj)` will return the methods, attributes, etc. of the object `obj` as a list of strings.

The following convenience function might prove to be useful sometimes.

```python
def no_dunder(obj, strict=False):
    prefix = "__" if strict else "_"
    return [s for s in dir(obj) if not s.startswith(prefix)]
```
