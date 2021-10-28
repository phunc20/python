## `ord()` and `chr()`

```python
In [1]: ord("お")
Out[1]: 12362

In [2]: [chr(code) for code in range(12353, 12500)]
Out[2]:
['ぁ',
 'あ',
 'ぃ',
 'い',
 'ぅ',
 'う',
 'ぇ',
 'え',
 'ぉ',
 'お',
 'か',
 'が',
 'き',
 'ぎ',
 'く',
 'ぐ',
 ...]
```


## 濁点と半濁点 (Dakuten and Handakuten)
<https://github.com/JeromeLefebvre/JapaneseCounting/issues/3>

It seems that
- Dakuten (i.e. 点々, `'ﾞ'`) has unicode `"\u3099"`
- Handakuten (i.e. 丸, `"ﾟ"`) has unicode`"\u309a"`
  ```
  In [54]: [chr(code) for code in range(12438, 12446)]
  Out[54]: ['ゖ', '\u3097', '\u3098', '゙', '゚', '゛', '゜', 'ゝ']
  ```
- `"\u309b"` and `"\u309c"` seems to be inappropriate (han)dakuten for most situations:
  ```
  In [159]: "\u309b"
  Out[159]: '゛'
  
  In [160]: "は" + "\u309b"
  Out[160]: 'は゛'
  
  In [161]: unicodedata.normalize("NFC", "は" + "\u309b")
  Out[161]: 'は゛'
  
  In [162]: len(unicodedata.normalize("NFC", "は" + "\u309b"))
  Out[162]: 2
  ```

Below is an example which might help quickly grasp the essentials.
```python
In [1]: ba = "は" + "\u3099"

In [2]: ba
Out[2]: 'ば'

In [3]: len(ba)
Out[3]: 2

In [4]: ba[0], ba[1]
Out[4]: ('は', '゙')

In [5]: ba_by_typing = "ば"

In [6]: ba_by_typing == ba
Out[6]: False

In [7]: import unicodedata

In [8]: unicodedata.normalize("NFC", ba) == ba_by_typing
Out[8]: True

In [9]: unicodedata.normalize('NFC', "ま" + "\u3099"*5)
Out[9]: 'ま゙゙゙゙゙'

In [10]: len(unicodedata.normalize('NFC', "ま" + "\u3099"*5))
Out[10]: 6

In [11]: unicodedata.normalize("NFD", ba_by_typing)[1] == ba[1]
Out[11]: True

In [12]: unicodedata.normalize("NFD", ba_by_typing)[0] == ba[0]
Out[12]: True
```

Recall that

- `"NFC"` stands for **Normal Form Compose**
- `"NFD"` stands for **Normal Form Decompose**

There are two Python scripts in `pwd`, namely `tenten_maru.py` and `dakuten.py`, that we
write to illustrate how to convert btw dakuten, handakuten and no-mark.

- `tenten_maru.py` will add dakuten and handakuten even to those hiragana or katakana that are illegitimate to bear dakuten or handakuten. `tenten_maru.py` uses `unicodedata`, in particular, the function `normalize()`
- `dakuten.py`, on the other hand, takes into consideration the legitimacy. Besides, `dakuten.py` only uses `ord()` and `chr()` and not `unicodedata`


## 全角と半角 (Zenkaku and Hankaku)
