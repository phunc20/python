## Bitwise Operators
https://wiki.python.org/moin/BitwiseOperators
Example of `&`:<br>
Have you ever thought about why code like `x & 0x1` can be used to test the parity of `x`,
where `x` is an `int`? Well, actually, `1` (or equiv. `0x1`, `0b1`, etc.) are thought of
as a binary number with only the least significant bit being `1` and `0` elsewere, as a 
consequence of which when we do the _binary bit-wise and_, all bits except the least significant
one are ignorant/untested, only the least significant bit being tested whether it's `0` or `1`.
```python
In [3]: 0b11
Out[3]: 3

In [4]: 3 & 0b11
Out[4]: 3

In [5]: 7 & 0b11
Out[5]: 3

In [6]: 0b11
Out[6]: 3

In [7]: 7 & 0b111
Out[7]: 7

In [8]: 7 & 0b110
Out[8]: 6
```

**(?1)** It seems that in Python, test of parity using
- `x % 2`
- `x & 0b1`
are equally fast. Why was that? A little source code, maybe?







