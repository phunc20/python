```python
Python 3.10.4 (main, Mar 31 2022, 03:38:35) [Clang 12.0.0 ]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: isinstance(True, int)
Out[1]: True

In [2]: isinstance(False, int)
Out[2]: True

In [3]: issubclass(bool, int)
Out[3]: True

In [4]: True is 1
<>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
<ipython-input-4-0acca4945321>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
  True is 1
Out[4]: False

In [5]: 1 is 1
<>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
<ipython-input-5-c4ba21148a2b>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
  1 is 1
Out[5]: True

In [6]: True == 1
Out[6]: True

In [7]: True == 1.0
Out[7]: True

In [8]: 1 == 1.0
Out[8]: True

In [9]: False is 0
<>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
<ipython-input-9-62d8d9e7196d>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
  False is 0
Out[9]: False

In [10]: 0 is 0
<>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
<ipython-input-10-c9bd0d8624de>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
  0 is 0
Out[10]: True

In [11]: False == 0
Out[11]: True

In [12]: False == 1
Out[12]: False

In [13]: True == 0
Out[13]: False

In [14]: True == 2
Out[14]: False

In [15]: True == -1
Out[15]: False

In [16]: True is True
Out[16]: True

In [17]: False is False
Out[17]: True
```
