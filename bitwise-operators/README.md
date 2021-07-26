# Bitwise Operators
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


## Left Shift `<<`
`a << n` is like `a * (2**n)` for all non-negative integers `n`.
- Don’t use the bit shift operators as a means of premature optimization in Python. You won’t see a difference in execution speed, but you’ll most definitely make your code less readable. This is because most compilers and interpreters today, including Python's, are quite capable of optimizing your code behind the scenes.


## `~`, i.e. Bitwise NOT
```
In [38]: 7 + ~7
Out[38]: -1

In [39]: ~7
Out[39]: -8

In [40]: for i in range(10):
    ...:     print(i + ~i)
    ...:
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
```


## `10`-Based and `2`-Based Number Conversion
- To enter an integer using `2`-based: e.g. the integer `11` is **`0b1011`**.
  - Note that prefixing zeros matters not.
    ```
    In [33]: 0b0001
    Out[33]: 1
    
    In [34]: 0b00000000000000001
    Out[34]: 1
    ```
  - There exists other ways to type `11` in base-`2`, for example, **`int("1011", 2)`** and **`int("0b1011", 2)`**.
- Conversely, to enter see the base-`2` form of an integer in base-`10` form, do **`bin(11)`**, whose output is a string -- **`"0b1011"`**.
  - To get rid of the prefix `0b`, it's quite simple: `bin(11)[2:]`

The following is an ipython session which helps to understand these.
```
In [25]: int("1011")
Out[25]: 1011

In [26]: int("1011", 2)
Out[26]: 11

In [27]: bin(11)
Out[27]: '0b1011'

In [28]: 0b1011
Out[28]: 11

In [29]: 0b1111
Out[29]: 15

In [30]: int(bin(11))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-30-ae36ce465c72> in <module>
----> 1 int(bin(11))

ValueError: invalid literal for int() with base 10: '0b1011'

In [31]: int(bin(11), 2)
Out[31]: 11

In [32]: int("0b1011", 2)
Out[32]: 11
```


## Notes
- Python's sign bit doesn't have a fixed position; there is no sign bit at all in Python.
