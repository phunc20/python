```python
In [5]: 0.3 + 0.1
Out[5]: 0.4

In [6]: 0.3 + 0.1 == (0.2 + 0.1) + 0.1
Out[6]: True

In [7]: 0.2 + 0.1
Out[7]: 0.30000000000000004

In [8]: 0.30000000000000004 == 0.3
Out[8]: False

In [15]: 0.1 + 0.1
Out[15]: 0.2

In [16]: 0.1 + 0.1 + 0.1
Out[16]: 0.30000000000000004

In [17]: 0.1 + 0.1 + 0.1 + 0.1
Out[17]: 0.4

In [18]: 0.1 + 0.1 + 0.1 + 0.1 + 0.1
Out[18]: 0.5

In [19]: 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
Out[19]: 0.6

In [20]: 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
Out[20]: 0.7

In [21]: 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
Out[21]: 0.7999999999999999
```




```python
In [31]: 1e-323 > 0
Out[31]: True

In [32]: 1e-324 > 0
Out[32]: False

In [33]: 1e-323 - sys.float_info.min
Out[33]: -2.2250738585072004e-308

In [34]: sys.float_info.min - 1e-323
Out[34]: 2.2250738585072004e-308

In [35]: sys.float_info.min - 1e-323 == sys.float_info.min
Out[35]: False

In [36]: sys.float_info.min
Out[36]: 2.2250738585072014e-308

In [37]: import math

In [38]: math.ulp()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In [38], line 1
----> 1 math.ulp()

TypeError: math.ulp() takes exactly one argument (0 given)
In [39]: math.ulp(0)
Out[39]: 5e-324

In [40]: list(pack('>d', sys.float_info.min))
Out[40]: [0, 16, 0, 0, 0, 0, 0, 0]

In [41]: list(pack('>d', math.ulp(0)))
Out[41]: [0, 0, 0, 0, 0, 0, 0, 1]

In [29]: "".join([f"{b:08b}" for b in pack(">d", sys.float_info.min)])
Out[29]: '0000000000010000000000000000000000000000000000000000000000000000'

In [30]: "".join([f"{b:08b}" for b in pack(">d", math.ulp(0))])
Out[30]: '0000000000000000000000000000000000000000000000000000000000000001'

In [43]: 2**(1-1023) == sys.float_info.min
Out[43]: True

In [49]: (1 + 2**-52) * 2**-1023 == math.nextafter(0,1)
Out[49]: False

In [62]: (2**-51) * (2**-1023)
Out[62]: 5e-324

In [63]: (2**-51) * (2**-1023) == math.nextafter(0,1)
Out[63]: True

In [22]: math.nextafter?
Signature: math.nextafter(x, y, /)
Docstring: Return the next floating-point value after x towards y.
Type:      builtin_function_or_method

In [23]: math.nextafter(0,1)
Out[23]: 5e-324

In [24]: math.nextafter(0,1) == math.ulp(0)
Out[24]: True

In [98]: bits = "1" + "0"*63

In [97]: minus0 = unpack(
    ...:     ">d",
    ...:     bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8)),
    ...: )[0]

In [98]: bits = "0"*64

In [99]: plus0 = unpack(
    ...:     ">d",
    ...:     bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8)),
    ...: )[0]

In [100]: plus0, minus0
Out[100]: (0.0, -0.0)

In [101]: plus0 == minus0
Out[101]: True

In [14]: sys.float_info.min == 2**-1022
Out[14]: True

In [16]: math.nextafter(0, 1) == 2**-52 * 2**-1022
Out[16]: True

In [20]: math.nextafter(sys.float_info.min, 0) == (1 - 2**-52) * 2**-1022
Out[20]: True
```


## Ref.
- <https://stackoverflow.com/questions/8341395/what-is-a-subnormal-floating-point-number>



## Other
Uniform distribution btw 0 and 1:
```python
In [21]: n_numbers_btw_0_and_1 = 2**52 * (1022+1)

In [22]: n_numbers_btw_0_and_1
Out[22]: 4607182418800017408

In [23]: 1/n_numbers_btw_0_and_1
Out[23]: 2.170523997312134e-19
```
