To test is a string consists entirely of char in `[a-zA-Z]` and other accented chars.
```python
In [13]: str.isalpha('Z')
Out[13]: True

In [14]: str.isalpha('a')
Out[14]: True

In [15]: str.isalpha('ấ')
Out[15]: True

In [16]: str.isalpha('ê')
Out[16]: True

In [17]: str.isalpha('ê ')
Out[17]: False

In [18]: str.isalpha('3')
Out[18]: False

In [19]: str.isalpha('%')
Out[19]: False

In [22]: str.isalpha('家')
Out[22]: True

In [23]: str.isalpha('家人')
Out[23]: True
```








