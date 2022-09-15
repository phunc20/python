Cf. <https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview>

> Only ASCII characters are permitted in bytes literals (regardless of the declared source code encoding). Any binary values over 127 must be entered into bytes literals using the appropriate escape sequence.
```python
In [41]: b"ế"
  File "<ipython-input-41-9e38d71a77c8>", line 1
    b"ế"
    ^
SyntaxError: bytes can only contain ASCII literal characters.
```






```python
In [17]: for k in range(10):
    ...:     print(f"sys.getsizeof(bytes({k})) = {sys.getsizeof(bytes(k))}")
    ...:
sys.getsizeof(bytes(0)) = 33
sys.getsizeof(bytes(1)) = 34
sys.getsizeof(bytes(2)) = 35
sys.getsizeof(bytes(3)) = 36
sys.getsizeof(bytes(4)) = 37
sys.getsizeof(bytes(5)) = 38
sys.getsizeof(bytes(6)) = 39
sys.getsizeof(bytes(7)) = 40
sys.getsizeof(bytes(8)) = 41
sys.getsizeof(bytes(9)) = 42

In [18]: for k in range(10):
    ...:     print(f"sys.getsizeof({k}) = {sys.getsizeof(k)}")
    ...:
sys.getsizeof(0) = 24
sys.getsizeof(1) = 28
sys.getsizeof(2) = 28
sys.getsizeof(3) = 28
sys.getsizeof(4) = 28
sys.getsizeof(5) = 28
sys.getsizeof(6) = 28
sys.getsizeof(7) = 28
sys.getsizeof(8) = 28
sys.getsizeof(9) = 28

In [19]: bytes(range(20))
Out[19]: b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13'

In [20]: b"\x09"
Out[20]: b'\t'

In [21]: b"\x0a"
Out[21]: b'\n'

In [22]: b"\x0d"
Out[22]: b'\r'

In [23]: "\t".encode("utf-8")
Out[23]: b'\t'

In [24]: "\n".encode("utf-8")
Out[24]: b'\n'

In [25]: "\n".encode("utf-8") == b"\x0a"
Out[25]: True
```
