

## Merging/Concatenating `SelectorList`s
Often one single XPath expression cannot capture all that we want.
We might need several of them. Since `response.xpath()`'s return
value is of type `SelectorList`

```python
$ scrapy shell "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E4%BC%81%E6%A5%AD%E4%B8%80%E8%A6%A7_(%E5%BB%BA%E8%A8%AD)#%E9%80%A0%E5%9C%92%E6%A5%AD%E8%80%85"

In [1]: len(response.xpath('//ul[preceding-sibling::*[1][name()="h3"]]'))
Out[1]: 10

In [2]: response.xpath('//ul[preceding-sibling::*[1][name()="h3"]]')
Out[2]:
[<Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E3%82%A2%E3%8...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E3%82%AC%E3%8...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E3%82%B5%E3%8...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/w/index.php?title=%...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E5%86%85%E8%9...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E9%96%93%E7%B...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E7%9C%9F%E6%9...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E5%AE%89%E6%B...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/w/index.php?title=%...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E8%8B%A5%E7%A...'>]

In [3]: type(response.xpath('//ul[preceding-sibling::*[1][name()="h3"]]'))
Out[3]: scrapy.selector.unified.SelectorList
```

and a `SelectorList` is similar to a Python list but with additional methods,
it's natural to want to concatenate them. Inspecting the methods of `SelectorList`,

```python
In [4]: sl = response.xpath('//ul[preceding-sibling::*[1][name()="h3"]]')

In [5]: [s for s in dir(sl) if not s.startswith("_")]
Out[5]:
['append',
 'attrib',
 'clear',
 'copy',
 'count',
 'css',
 'extend',
 'extract',
 'extract_first',
 'get',
 'getall',
 'index',
 'insert',
 'pop',
 're',
 're_first',
 'remove',
 'reverse',
 'sort',
 'xpath']
```

it is not hard to notice that we seem to be able to `extend` or `append` a `SelectorList`
like we do to normal Python lists! And indeed,

```python
In [6]: len(response.xpath('//ul[preceding-sibling::*[1][name()="h2" and ./span[@class="mw-headline"]/text()!="関連項目"]]'))
Out[6]: 1

In [7]: response.xpath('//ul[preceding-sibling::*[1][name()="h2" and ./span[@class="mw-headline"]/text()!="関連項目"]]')
Out[7]: [<Selector xpath='//ul[preceding-sibling::*[1][name()="h2" and ./span[@class="mw-headline"]/text()!="関連項目"]]' data='<ul><li>株式会社山梅（本社:群馬県太田市)</li>\n<li>株式...'>]

In [8]: len(sl)
Out[8]: 10

In [9]: sl.extend(response.xpath('//ul[preceding-sibling::*[1][name()="h2" and ./span[@class="mw-headline"]/text()!="関連項目"]]'))

In [10]: len(sl)
Out[10]: 11

In [11]: sl
Out[11]:
[<Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E3%82%A2%E3%8...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E3%82%AC%E3%8...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E3%82%B5%E3%8...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/w/index.php?title=%...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E5%86%85%E8%9...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E9%96%93%E7%B...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E7%9C%9F%E6%9...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E5%AE%89%E6%B...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/w/index.php?title=%...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h3"]]' data='<ul><li><a href="/wiki/%E8%8B%A5%E7%A...'>,
 <Selector xpath='//ul[preceding-sibling::*[1][name()="h2" and ./span[@class="mw-headline"]/text()!="関連項目"]]' data='<ul><li>株式会社山梅（本社:群馬県太田市)</li>\n<li>株式...'>]
```

This way one could still profit from using the `SelectorList` methods of `sl`, in particular, `get`, `getall`, etc.
