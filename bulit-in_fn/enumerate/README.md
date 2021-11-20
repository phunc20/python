The function `enumerate()` accepts an optional integer argument, which stands for the first index it returns,
all subsequent indices are incremented by `1` at each iteration.
```python
In [1]: L = ["alice", "bob", "charlie"]

In [2]: for i, name in enumerate(L):
   ...:     print(i, name)
   ...:
0 alice
1 bob
2 charlie

In [3]: for i, name in enumerate(L, 1):
   ...:     print(i, name)
   ...:
1 alice
2 bob
3 charlie

In [4]: for i, name in enumerate(L, -3):
   ...:     print(i, name)
   ...:
-3 alice
-2 bob
-1 charlie
```
