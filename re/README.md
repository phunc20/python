### Why using raw strings to specify regex?
Let's first look at the following example.
```python
In [28]: s = "This \\n is not a new line character but two backslash followed by an n"

In [29]: print(s)
This \n is not a new line character but two backslashes followed by an n

In [30]: re.findall(r"\n", s)
Out[30]: []

In [31]: re.findall(r"\\n", s)
Out[31]: ['\\n']

In [32]: print(r"\n")
\n

In [33]: re.findall("\n", s)
Out[33]: []

In [34]: re.findall("\\n", s)
Out[34]: []

In [35]: re.findall("\\\n", s)
Out[35]: []

In [36]: re.findall("\\\\n", s)
Out[36]: ['\\n']

In [37]: print(r"\n")
\n

In [38]: print(r"\\n")
\\n

In [39]: print("\\n")
\n

In [40]: print("\\\\n")
\\n
```



### `search()` only searches the first match
For example,
```python

In [1]: import re

In [2]: string = "398202 123, 2392 1111"

In [3]: pattern = "(\d{3}) (\d{2})"

In [4]: match = re.search(pattern, string)

In [6]: match.group()
Out[6]: '202 12'

In [7]: match.group(1)
Out[7]: '202'

In [8]: match.group(2)
Out[8]: '12'

In [9]: re.findall(pattern, string)
Out[9]: [('202', '12'), ('392', '11')]
```


