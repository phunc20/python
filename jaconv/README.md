# What is `jaconv`?


## Hiragana-Katakana Conversion
```python
import jaconv

# Hiragana to Katakana
jaconv.hira2kata('ともえまみ')
# => 'トモエマミ'

# Hiragana to half-width Katakana
jaconv.hira2hkata('ともえまみ')
# => 'ﾄﾓｴﾏﾐ'

# Katakana to Hiragana
jaconv.kata2hira('巴マミ')
# => '巴まみ'
```

`jaconv` could do the above conversions and more
(cf. <https://pypi.org/project/jaconv/>).


## Zenkaku (i.e. Full-Width) to Hankaku (i.e. Half-Width)
- Signature: `jaconv.z2h(text, ignore='', kana=True, ascii=False, digit=False)`
- There is `z2h` and `h2z`, standing for "zenkaku to hankaku" and
  for "hankaku to zenkaku", resp.

```python
In [24]: s = 'ＴＡＫＥ\u3000ＳＴＯＣＫ'

In [25]: jaconv.z2h(s)
Out[25]: 'ＴＡＫＥ\u3000ＳＴＯＣＫ'

In [26]: jaconv.z2h(s, ascii=True)
Out[26]: 'TAKE STOCK'

In [27]: jaconv.h2z(jaconv.z2h(s, ascii=True), ascii=True) == s
Out[27]: True
```

**Rmk.**  
1. The boolean options include `kana, ascii, digit` and only `kana` is ON by default.
    - Note that there is **NO hiragana**, i.e. hiragana seems to be always half-width in
      Japanese.
1. The **full-width space character** `"\u3000"` can also be converted to half-width
   by demanding `ascii=True` with `jaconv.z2h`.
   ```python
   In [32]: t = '１２３４\u3000５６７８'
   
   In [32]: jaconv.z2h(t, digit=True)
   Out[32]: '1234\u30005678'
   
   In [33]: jaconv.z2h(t, ascii=True)
   Out[33]: '１２３４ ５６７８'
   
   In [34]: jaconv.z2h(t, kana=True)
   Out[34]: '１２３４\u3000５６７８'

   In [35]: jaconv.h2z(" ", ascii=True)
   Out[35]: '\u3000'
   
   In [36]: jaconv.h2z(" ")
   Out[36]: ' '
   
   In [37]: jaconv.h2z(" ", digit=True)
   ```
