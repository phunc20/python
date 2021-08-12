Self-defined class instances can also be compared using `<, <=, ==, >, >=`.
It suffices to define the corresponding methods:

| binary op | method |
|-----------|--------|
| `<` | `__lt__` |
| `<=` | `__le__` |
| `==` | `__eq__` |
| `>` | `__gt__` |
| `>=` | `__ge__` |


I have written a demo file `demo.py` to illustrate this. The script defines
two classes which both have attributes like 2D Cartesian coordinates, and
we want to define an order for these coordinates such that, if we go
in increasing order, we should go

- from left to right
- from top to bottom

That is, those coordinates whose have bigger `y`'s will bigger; for those coordinates
with approximately the same `y`, we compare their `x`-coordinates.

The `demo.py` script can be run on any machine with Python version greater than or equal to `3.6` like follows.

```bash
(oft) ~/.../python/class/__lt__$ python demo.py
---> print(sorted([B, D, A, C]))
TypeError: '<' not supported between instances of 'Coord' and 'Coord'

sorted("bdac", key=lambda char: L[ord(char) - ord('a')]) = ['a', 'b', 'd', 'c']

sorted([Q, S, P, R]) = [P, Q, R, S]
(oft) ~/.../python/class/__lt__$
```
