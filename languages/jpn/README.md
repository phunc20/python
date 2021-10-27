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


## Dakuten and handakuten
<https://github.com/JeromeLefebvre/JapaneseCounting/issues/3>

It seems that
- Dakuten (i.e. 点々, `'ﾞ'`) has unicode `"\u3099"`
- Handakuten (i.e. 丸, `"ﾟ"`) has unicode`"\u3100"`
  ```
  In [54]: [chr(code) for code in range(12438, 12446)]
  Out[54]: ['ゖ', '\u3097', '\u3098', '゙', '゚', '゛', '゜', 'ゝ']
  ```

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
