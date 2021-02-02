



## Decreasing
Instead of, say, `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, the range of `range(0, 10+1)`, sometimes,
we might find situations in which it is more convenient to iterate through its reverse order, i.e.
`[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]`. Here below are a few ways to do it.
```python
In [20]: list(range(10,-1,-1))
Out[20]: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

In [21]: reversed(range(0, 10+1))
Out[21]: <range_iterator at 0x7f5ae4d02600>

In [22]: list(reversed(range(0, 10+1)))
Out[22]: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

```
**Note.** If what one wants is to iterate thru the integers, there is no need for the `list()`; it's there so that
we can print them in the REPL.
