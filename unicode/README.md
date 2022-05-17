```python
In [2]: "\N{GREEK CAPITAL LETTER DELTA}"
Out[2]: 'Δ'

In [3]: "\u0394"
Out[3]: 'Δ'

In [4]: "\u00000394"
Out[4]: '\x000394'

In [5]: "\U00000394"
Out[5]: 'Δ'

In [6]: "\U000394"
  File "<ipython-input-6-a7df9ec57000>", line 1
    "\U000394"
    ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-7: truncated \UXXXXXXXX escape
```

- `"\u0394"` is called a **16-bit hex value** because we have 4 hexadecimal digits, making a total of
  `(16)**4 = 2**16`
- `"\U00000394"` [Note the capital `U` and the number of digits] is called a **32-bit hex value** because
  this time we have 8 hexadecimal digits, making a total of `(16)**8 = 2**32`


## `decode`
Signature
```
decode(encoding, errors)
    encoding, e.g. "utf-8"
    errors, e.g. "strict", "replace", "backslashreplace", "ignore"
```

Example
```python
In [9]: b'\x80abc'.decode("utf-8", "replace")
Out[9]: '�abc'

In [10]: "\ufffd"
Out[10]: '�'

In [11]: b'\x80abc'.decode("utf-8", "backslashreplace")
Out[11]: '\\x80abc'

In [12]: len(b'\x80abc'.decode("utf-8", "backslashreplace"))
Out[12]: 7

In [13]: len(b'\x80abc')
Out[13]: 4

In [14]: len(b'\x80abc'.decode("utf-8", "replace"))
```
