> Chinese and Japanese character costs usually `3` bytes in UTF-8 encoding, whereas each English character only
> costs `1` bytes ($16\cdot 16 = 256 = 2^8$).

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

In [8]: len(discontinuous.encode("utf-8"))
Out[8]: 210

In [9]: len(discontinuous.encode("utf-16"))
Out[9]: 142

In [10]: len(discontinuous.encode("utf-32"))
Out[10]: 284
```


In UTF-8,

- characters, like `"ç", "ê"`, costs `2` bytes each
- Japanese kanji/katagana/hiragana, regardless of being full-width or half-width,
  seems to cost `3` bytes each

```
In [8]: " ".encode("utf-8")
Out[8]: b' '

In [9]: "　".encode("utf-8")
Out[9]: b'\xe3\x80\x80'

In [10]: "ｱｲｳｴｵ".encode("utf-8")
Out[10]: b'\xef\xbd\xb1\xef\xbd\xb2\xef\xbd\xb3\xef\xbd\xb4\xef\xbd\xb5'

In [11]: len(_)
Out[11]: 15

In [12]: len("€uro")
Out[12]: 4

In [13]: len("€uro".encode("utf-8"))
Out[13]: 6

In [14]: type("€uro".encode("utf-8"))
Out[14]: bytes

In [15]: for char in "€uro":
    ...:     print(char, len(char.encode("utf-8")))
    ...:
€ 3
u 1
r 1
o 1
```
