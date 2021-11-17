# What is `jaconv`?
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

`jaconv` could do the above conversions and more (cf. <https://pypi.org/project/jaconv/>).
It is useful if your code deals with Japanese a lot.
