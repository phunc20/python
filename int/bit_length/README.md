## The Method `bit_length()` of The Class of `int`
To obtain the bit length when expressing an integer in base-`2` form, one can call the method
`bit_length()`.

```
In [75]: 1234.bit_length()
  File "<ipython-input-75-b77dbdef4b69>", line 1
    1234.bit_length()
                  ^
SyntaxError: invalid syntax


In [76]: !which python
/home/phunc20/miniconda3/envs/py3.6/bin/python

In [77]: int.bit_length(1234)
Out[77]: 11

In [78]: (1234).bit_length()
Out[78]: 11

In [79]: (255).bit_length()
Out[79]: 8

In [80]: (5).bit_length()
Out[80]: 3

In [81]: (2**5-1).bit_length()
Out[81]: 5

In [82]: (2**5).bit_length()
Out[82]: 6
```

**Rmk.**
- For literal integers, surround it with **parentheses**, e.g. `(42).bit_length()` instead of
  `42.bit_length()`. Otherwise, one can also do `int.bit_length(42)`.
- I think `bit_length(a)` will be faster than `len(bin(a)) - 2`, where `a` is an integer. Let's
  test this.
  ```
  In [79]: %%timeit
      ...: for i in range(1_000):
      ...:     i.bit_length()
      ...:
  
  179 µs ± 1.23 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
  
  In [80]:
  
  In [80]: %%timeit
      ...: for i in range(1_000):
      ...:     len(bin(i)) - 2
      ...:
  419 µs ± 1.33 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
  ```
  Indeed, our guess is confirmed.


