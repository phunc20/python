## As A Data Structure for Storing Images
From MIT's 6.006 course, I realized that we can actually use the Python dictionary
as a means to store image data:

```python
In [1]: D = dict()

In [2]: D[0, 0] = 255

In [3]: D[0, 1] = 120

In [4]: D
Out[4]: {(0, 0): 255, (0, 1): 120}

In [5]:
```

To put in simpler terms, the assignment `D[0, 0] = 255` is not diff from
`D[(0, 0)] = 255`






