## `dict` to `pd.DataFrame`
The following is a common scenario in which one wants to put

- the dictionary keys into the indices of a DataFrame
- the dictionary values into the values of each column

```python
D1 = {
    "height": 175.5,
    "weight": 80.4,
}
D2 = {
    "height": 157.8,
    "weight": 50.9,
}
s1 = pd.Series(D1)
s2 = pd.Series(D2)

import pandas as pd
df = pd.DataFrame({
    "Alice": s1,
    "Bob": s2,
})

>>> df
        Alice   Bob
height  175.5  157.8
weight  80.4   50.9
```
