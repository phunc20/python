## The Same Copies of Sth
List comprehension could be used to create different copies of the same thing multiple times.
```python
In [1]: L = [{"x": 220, "y": 7}] * 4

In [2]: L[0]["y"] = -1

In [3]: L
Out[3]:
[{'x': 220, 'y': -1},
 {'x': 220, 'y': -1},
 {'x': 220, 'y': -1},
 {'x': 220, 'y': -1}]

In [4]: set(id(D) for D in L)
Out[4]: {140478471587520}

In [5]: L = [{"x": 220, "y": 7} for _ in range(4)]

In [6]: L[0]["y"] = -1

In [7]: L
Out[7]:
[{'x': 220, 'y': -1},
 {'x': 220, 'y': 7},
 {'x': 220, 'y': 7},
 {'x': 220, 'y': 7}]

In [8]: set(id(D) for D in L)
Out[8]: {140478462849216, 140478471587328, 140478471734784, 140478480968832}
```


## With Two `for`'s
```python
In [17]: [(i, j) for i in range(3) for j in range(-1,-4,-1)]
Out[17]:
[(0, -1),
 (0, -2),
 (0, -3),
 (1, -1),
 (1, -2),
 (1, -3),
 (2, -1),
 (2, -2),
 (2, -3)]
```


