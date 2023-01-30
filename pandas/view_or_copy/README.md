```python
In [1]: import pandas as pd

In [2]: df = pd.DataFrame({"name": ["Antoniño"], "country": ["Brazin"], "age": [32.1]})

In [3]: df
Out[3]:
       name country   age
0  Antoniño  Brazin  32.1

In [4]: df.iloc[0][0] = "Antonio"
<ipython-input-4-a3620435bf0b>:1: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a
-copy
  df.iloc[0][0] = "Antonio"

In [5]: df
Out[5]:
       name country   age
0  Antoniño  Brazin  32.1

In [6]: df["name"][0] = "Antonio"
<ipython-input-6-0cc50bac295d>:1: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df["name"][0] = "Antonio"

In [7]: df
Out[7]:
      name country   age
0  Antonio  Brazin  32.1

In [8]: df.iloc[0]._is_view
Out[8]: False

In [9]: df["name"]._is_view
Out[9]: True

In [10]: df.iloc[0,1] = "Brazil"

In [11]: df
Out[11]: 
      name country   age
0  Antonio  Brazil  32.1

In [12]: df = pd.DataFrame({"name": ["Antoniño"], "country": ["Brazin"]})

In [13]: df.iloc[0][0] = "Antonio"

In [14]: df
Out[14]: 
      name country
0  Antonio  Brazin

In [15]: df.iloc[0]._is_view
Out[15]: True

In [16]: df["name"]._is_view
Out[16]: True
```

- Correct doing: `df.iloc[i, j] = sth`
- Wrong doing: `df.iloc[i][j] = sth` because we are not sure whether this modifies `df` or not.
  Besides, this consists of two operations instead of one.

ipdb> df.iloc[-3, :]._is_view
False
ipdb> df.iloc[:, -4]._is_view
True
ipdb> df.loc[:, "left"]._is_view
