> Chinese and Japanese characters cost usually three bytes in UTF-8 encoding.

Let's verify this.

```ipython
In [2]: len("拼")
Out[2]: 1

In [3]: len("拼".encode("utf-8"))
Out[3]: 3

In [4]: "拼".encode("utf-8")
Out[4]: b'\xe6\x8b\xbc'

In [5]: discontinuous = "数学において、線型写像は線型空間の「単に」代数構造を保つ写像の重要なクラスを成し、またより一般の写像を近似するのにも用いられる（一次近似）。"

In [6]: len(discontinuous)
Out[6]: 70

In [7]: for char in discontinuous:
   ...:     encoded = char.encode("utf-8")
   ...:     if len(encoded) != 3:
   ...:         print(f"{char}, {encoded}, {len(encoded)}")
   ...:

In [8]:
```
