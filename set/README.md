## What Kind of Object Can Figure in A Set/Dictionary-Key?
```
In [1]: S = set()

In [2]: S.add([1,2,3])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-4aade7c1a1f8> in <module>
----> 1 S.add([1,2,3])

TypeError: unhashable type: 'list'

In [3]: S.add((1,2,3))
```
