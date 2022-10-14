
```python
In [6]: from struct import pack, unpack

In [7]: pack("bb", 42)
---------------------------------------------------------------------------
error                                     Traceback (most recent call last)
Input In [7], in <cell line: 1>()
----> 1 pack("bb", 42)

error: pack expected 2 items for packing (got 1)

In [8]: pack("bb", -42, 42)
Out[8]: b'\xd6*'

In [9]: pack("2b", -42, 42)
Out[9]: b'\xd6*'

In [10]: pack("b", 42)
Out[10]: b'*'

In [11]: type(pack("b", 42))
Out[11]: bytes
```
