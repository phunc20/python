Sometimes, you may want to save a file with timestamp in its file name.
In this case, the `strftime` method of the `datetime` class may be used.
```python
In [1]: from datetime import datetime

In [2]: datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")
Out[2]: '2023-09-16_21h55m47s'
```
