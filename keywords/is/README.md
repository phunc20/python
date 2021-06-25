# `is`
- Immutables are the same objects $\implies$ their `is` result gives `True`
- Mutables' `is` results are `False`
- `True`, `False` and `None` in Python all refers to the same objects, respectively.

```ipython
Python 3.7.10 (default, Feb 26 2021, 18:47:35)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.22.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: True is True
Out[1]: True

In [2]: False is False
Out[2]: True

In [3]: None is None
Out[3]: True

In [4]: is_handsome = True

In [5]: is_fat = True

In [6]: is_handsome is is_fat
Out[6]: True

In [7]: money = None

In [8]: houses = None

In [9]: money is houses
Out[9]: True

In [10]: [] is []
Out[10]: False

In [11]: [] == []
Out[11]: True

In [12]: {} is {}
Out[12]: False

In [13]: {} == {}
Out[13]: True

In [14]: (,) is (,)
  File "<ipython-input-14-5aff21783294>", line 1
    (,) is (,)
     ^
SyntaxError: invalid syntax


In [15]: () is ()
Out[15]: True

In [16]: () is None
Out[16]: False

In [17]: () == None
Out[17]: False

In [18]: type(())
Out[18]: tuple

In [19]: () == ()
Out[19]: True

In [20]: "" == ""
Out[20]: True

In [21]: "" is ""
Out[21]: True

In [22]: "abc" is "abc"
Out[22]: True

In [23]: name = "Galilei"

In [24]: middlename = "Galilei"

In [25]: name is middlename
Out[25]: True

In [26]: ("a" * 100) is ("a" * 100)
Out[26]: True
```

## Ref
- <https://www.programiz.com/python-programming/keyword-list#is>
