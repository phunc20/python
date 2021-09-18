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

In [8]:
```


In UTF-8,

- characters, like `"ç", "ê"`, costs `2` bytes each
- Japanese kanji/katagana/hiragana, regardless of being full-width or half-width, costs `3` bytes each

```
In [8]: " ".encode("utf-8")
Out[8]: b' '

In [9]: "　".encode("utf-8")
Out[9]: b'\xe3\x80\x80'

In [10]: "Essaye le français peut-être.".encode("utf-8")
Out[10]: b'Essaye le fran\xc3\xa7ais peut-\xc3\xaatre.'

In [11]: "ｱｲｳｴｵ".encode("utf-8")
Out[11]: b'\xef\xbd\xb1\xef\xbd\xb2\xef\xbd\xb3\xef\xbd\xb4\xef\xbd\xb5'

In [12]: len(_)
Out[12]: 15
```
