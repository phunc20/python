

### With <code>float</code>
just remember to count <b>the number of characters</b> right.
```python
In [1]: a = -20.1
In [2]: b = -1.0
In [3]: c = 0.0

In [4]: print(f"{a}\n{b}")
-20.1
-1.0

In [5]: print(f"{a:3.1f}\n{b}")
-20.1
-1.0

In [6]: print(f"{a:3.1f}\n{b:3.1f}")
-20.1
-1.0

In [7]: print(f"{a:4.1f}\n{b:4.1f}")
-20.1
-1.0


In [8]: print(f"{a:4.1f}\n{b:4.1f}\n{c:4.1f}")
-20.1
-1.0
 0.0

In [9]: print(f"{a:4.1f}\n{b:5.1f}\n{c:4.1f}")
-20.1
 -1.0
 0.0

In [10]: print(f"{a:5.1f}\n{b:5.1f}\n{c:4.1f}")
-20.1
 -1.0
 0.0

In [11]: print(f"{a:5.1f}\n{b:5.1f}\n{c:5.1f}")
-20.1
 -1.0
  0.0
```

### The same with <code>int</code>
```python
In [12]: a = 1

In [13]: b = -10

In [14]: c = -3

In [15]: d = 10

In [16]: print(f"{a}\n{b}\n{c}\n{d}")
1
-10
-3
10

In [17]: print(f"{a:2d}\n{b:2d}\n{c:2d}\n{d:2d}")
 1
-10
-3
10

In [18]: print(f"{a:3d}\n{b:3d}\n{c:3d}\n{d:3d}")
  1
-10
 -3
 10
```

