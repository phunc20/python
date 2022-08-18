> Only ASCII characters are permitted in bytes literals (regardless of the declared source code encoding). Any binary values over 127 must be entered into bytes literals using the appropriate escape sequence.
```python
In [41]: b"ế"
  File "<ipython-input-41-9e38d71a77c8>", line 1
    b"ế"
    ^
SyntaxError: bytes can only contain ASCII literal characters.
```
