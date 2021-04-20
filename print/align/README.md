
### With `str`
In formated strings, to pad a variable of type `str` with white spaces on the left, do
**`f"{string:>7}"`**, which will pad `7` white spaces for the variable `string`. This can also
be written using other syntaxes.

- `"{:>7}".format(string)`
- `"%7s" % string`

```
In [4]: str_len3 = "abc"; str_len4 = "wxyz"

In [5]: print(f"{str_len3:>4}", f"{str_len4:>max(str_len3, str_len4)}", sep="\n")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-5-05d72a72d588> in <module>
----> 1 print(f"{str_len3:>4}", f"{str_len4:>max(str_len3, str_len4)}", sep="\n")

ValueError: Invalid format specifier

In [6]: print(f"{str_len3:>4}", f"{str_len4:>4}", sep="\n")
 abc
wxyz
```


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

