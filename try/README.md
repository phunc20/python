## FAQ
- How to catch and reprint the cause of an error?
  ```python
  try:
      do_sth()
  except Exception as e:
      print(f"{e.__class__.__name__}: {e}")
  ```
- Exception handling (i.e. `try`) is slower than conditional evaluation (i.e. `if`)?
  **Yes**, if the `except` block is often catched. Indeed,
  ```python
  In [1]: D = dict(zip("abc", range(3))); D
  Out[1]: {'a': 0, 'b': 1, 'c': 2}
  
  In [2]: %%timeit
     ...: try:
     ...:     a = D["a"]
     ...: except KeyError:
     ...:     a = -1
     ...:
  52.8 ns ± 0.259 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
  
  In [3]: %%timeit
     ...: if "a" in D:
     ...:     a = D["a"]
     ...: else:
     ...:     a = -1
     ...:
  101 ns ± 0.896 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
  
  In [4]: %%timeit
     ...: if "z" in D:
     ...:     z = D["z"]
     ...: else:
     ...:     z = -1
     ...:
  51.6 ns ± 1.18 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
  
  In [5]: %%timeit
     ...: try:
     ...:     z = D["z"]
     ...: except KeyError:
     ...:     z = -1
     ...:
  271 ns ± 1.84 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
  ```

