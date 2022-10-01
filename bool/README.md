```python
In [1]: True is 1
<>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
<ipython-input-1-0acca4945321>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
  True is 1
Out[1]: False

In [2]: True is True
Out[2]: True

In [3]: 1 is 1
<>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
<ipython-input-3-c4ba21148a2b>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
  1 is 1
Out[3]: True

In [4]: False is None
Out[4]: False

In [5]: True == 1
Out[5]: True

In [6]: True == 0
Out[6]: False

In [7]: True == 2
Out[7]: False

In [8]: True == 3.1
Out[8]: False

In [9]: False == 0
Out[9]: True

In [10]: False == 0.0
Out[10]: True

In [11]: 0 == 0.0
Out[11]: True

In [14]: 0 == 0.00000000000000000000000000000000000000000000001
Out[14]: False

In [15]: 1 + 0.00000000000000000000000000000000000000000000001 == 1
Out[15]: True

In [16]: 0 == 0.0000000000000000000000000000000000000000000000
Out[16]: True

In [17]: 0.00000000000000000000000000000000000000000000001
Out[17]: 1e-47

In [18]: 0 == 1e-100
Out[18]: False

In [19]: 0 == 1e-1000
Out[19]: True

In [29]: 0 == 1e-323
Out[29]: False

In [30]: 0 == 1e-324
Out[30]: True
```
