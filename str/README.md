## Raw String
Escape characters like `\` in `\n`, `\t`, etc.

- are _convenient_ when we want to easily add newlines, indentations, etc.
- are _inconvenient_ when we want to print a lot of backslashes, e.g. in regex.

Raw strings (i.e. strings with an `r` or `R` in front: `r""`, `R""`) render
convenient the second case.

```python
In [23]: print(r"\n")
\n

In [24]: print(r"\\n")
\\n

In [25]: print(r"\\n\\t\t")
\\n\\t\t

In [26]: R"\n"
Out[26]: '\\n'

In [27]: r"\n"
Out[27]: '\\n'
```


## Byte String
Borrowed from <https://stackoverflow.com/questions/6224052/what-is-the-difference-between-a-string-and-a-byte-string> 

> Assuming Python 3 (in Python 2, this difference is a little less well-defined),
> a string is a sequence of characters, i.e.
> [unicode codepoints](http://en.wikipedia.org/wiki/Unicode);
> these are an _abstract concept_, and _can't be directly stored on disk_.
> A byte string is a sequence of, unsurprisingly, bytes - things that
> _can be stored on disk_. The mapping between them is an _encoding_ -
> there are quite a lot of these (and infinitely many are possible) -
> and you need to know which applies in the particular case in order to
> do the conversion, since a different encoding may map the same bytes to
> a different string:

```python
In [30]: s = "猫に小判"

In [31]: bs_utf8 = s.encode("utf-8")

In [32]: bs_utf8.decode("utf-16")
Out[32]: '賧\ue3abꮁ냥\ue58fꒈ'

In [33]: print(bs_utf8.decode("utf-16"))
賧ꮁ냥ꒈ

In [34]: print(bs_utf8.decode("utf-8"))
猫に小判

In [35]: bs_utf8.decode("utf-8")
Out[35]: '猫に小判'

In [36]: bs_utf16 = s.encode("utf-16")

In [37]: bs_utf16.decode("utf-8")
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-37-8d36ca1df5d1> in <module>
----> 1 bs_utf16.decode("utf-8")

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

In [38]: bs_utf16.decode("utf-16")
Out[38]: '猫に小判'
```

Note that sometimes characters typed with diff input methods may coincide
(here Chinese and Japanese character `小`)
```python
In [48]: "日本語小猫"[3].encode("utf-8")
Out[48]: b'\xe5\xb0\x8f'

In [49]: "中文小貓"[2].encode("utf-8")
Out[49]: b'\xe5\xb0\x8f'
```
