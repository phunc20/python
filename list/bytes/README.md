```python
In [65]: big_endian = b"\x00\x00\x07\xb1"

In [66]: list(big_endian)
Out[66]: [0, 0, 7, 177]

In [67]: bytes([0, 0, 7, 177])
Out[67]: b'\x00\x00\x07\xb1'
```
