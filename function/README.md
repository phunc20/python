## Pass-by-sharing
From inside a function, Python as well as Julia, function arguments are not copied. Instead,
they refer to the same objects in the caller; inside callee function, the arguments are simply
new variables referring to the same values. Consequently, if the arguments are of mutable data
structure, e.g. `list`, `dict`, etc. and if the function mutates/changes them from inside the
function, then the referred object will be changed.

```python
In [10]: def pass_by(sth):
    ...:     print(f"id(sth) = {id(sth)}")
    ...:

In [11]: T = (1,2,3)

In [12]: id(T)
Out[12]: 140478462525888

In [13]: pass_by(T)
id(sth) = 140478462525888

In [14]: L = [1,2,3]

In [15]: id(L)
Out[15]: 140478462802368

In [16]: pass_by(L)
id(sth) = 140478462802368
```
