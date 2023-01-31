# View or Copy
There is this property/attribute of all `pd.DataFrame`s
named `_is_view`, which could help us see whether the
sub-dataframe we extract from the dataframe is a view or
a copy.

Because the columns of a dataframe usually stores data of
the same data type,
- single-column extraction is a view
- cross-column is a copy

For example,
```python
In [1]: import pandas as pd

In [2]: pd.__version__
Out[2]: '1.4.4'

In [3]: df = pd.DataFrame({
   ...:     "name": ["Antoniño", "Chris"],
   ...:     "country": ["Brazin", "France"],
   ...:     "age (year)": [32.1, 25],
   ...:     "height (cm)": [178, 175],
   ...: })
   ...:

In [4]: df
Out[4]:
       name country  age (year)  height (cm)
0  Antoniño  Brazin        32.1          178
1     Chris  France        25.0          175

In [5]: df.dtypes
Out[5]:
name            object
country         object
age (year)     float64
height (cm)      int64
dtype: object

In [6]: df[["age (year)", "height (cm)"]]
Out[6]:
   age (year)  height (cm)
0        32.1          178
1        25.0          175

In [7]: df.loc[:, ["age (year)", "height (cm)"]]
Out[7]:
   age (year)  height (cm)
0        32.1          178
1        25.0          175

In [8]: df.loc[:, ["age (year)", "height (cm)"]]._is_view
Out[8]: False

In [9]: df[["age (year)", "height (cm)"]]._is_view
Out[9]: False

In [10]: df[["age (year)"]]
Out[10]: 
   age (year)
0        32.1
1        25.0

In [11]: df["age (year)"]
Out[11]: 
0    32.1
1    25.0
Name: age (year), dtype: float64

In [12]: type(df[["age (year)"]])
Out[12]: pandas.core.frame.DataFrame

In [13]: type(df["age (year)"])
Out[13]: pandas.core.series.Series

In [14]: type(df.loc[:, ["age (year)"]])
Out[14]: pandas.core.frame.DataFrame

In [15]: type(df.loc[:, "age (year)"])
Out[15]: pandas.core.series.Series

In [16]: df[["age (year)"]]._is_view
Out[16]: True

In [17]: df["age (year)"]._is_view
Out[17]: True

In [18]: df.loc[:, "age (year)"]._is_view
Out[18]: True

In [19]: df.loc[:, ["age (year)"]]._is_view
Out[19]: True
```


## Assignment (of Existing Entries)
Special attention needs to be paid during assignment.
Indeed, we
- shouldn't assign to a copy
- should always make sure to assign to a view

This is because, say, `df` and `df_sub` are the dataframe
in question and one of its sub-dataframe in copy, then
assigning to new values to elements of `df_sub` will not
modify the corresponding elements in `df`.

Pandas implements some warning messages when the user
does assignment on copies.

Before introducing an example, let's review Pandas' `.iloc`.
In particular, when we write `df.iloc[0]`, we are referring
to its **first row**, not its first column, whence
`df.iloc[0]` is destined to be a copy, not a view.  
Do watch that out!

Continuing on the same example above,
```python
In [20]: df.iloc[0]
Out[20]:
name           Antoniño
country          Brazin
age (year)         32.1
height (cm)         178
Name: 0, dtype: object

In [21]: df.iloc[:,0]
Out[21]:
0    Antoniño
1       Chris
Name: name, dtype: object

In [22]: df.iloc[:,0]._is_view
Out[22]: True

In [23]: df.iloc[0]._is_view
Out[23]: False
```

Similarly, putting list gives a dataframe and putting single
index gives a series.
```python
In [24]: type(df.iloc[:,0])
Out[24]: pandas.core.series.Series

In [25]: type(df.iloc[:,[0]])
Out[25]: pandas.core.frame.DataFrame

In [26]: type(df.iloc[0])
Out[26]: pandas.core.series.Series

In [27]: type(df.iloc[[0]])
Out[27]: pandas.core.frame.DataFrame
```

Ok, back to assignment. Here are a few good and bad examples:
```python
In [28]: df.iloc[0][0]
Out[28]: 'Antoniño'

In [29]: df.iloc[0][0] = "Antony"
<ipython-input-56-4d03b8ab170c>:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df.iloc[0][0] = "Antony"

In [30]: df
Out[30]: 
       name country  age (year)  height (cm)
0  Antoniño  Brazin        32.1          178
1     Chris  France        25.0          175
```

We see that the assignment does not change `"Antoniño"` to `"Antony"`. Why is that?

Well, because `iloc[0]` gives a copy and we are assigning
`"Antony"` to that new copy, whence `df` remains intact.

One correct way to do this is as follows:
```python
In [31]: df.iloc[0,0] = "Antony"

In [32]: df
Out[32]: 
     name country  age (year)  height (cm)
0  Antony  Brazin        32.1          178
1   Chris  France        25.0          175
```

Let's do one last assignment: `"Brazin"` to `"Brazil"`
```python
In [33]: df["country"][0] = "Brazil"
<ipython-input-87-3dd77b4b9616>:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df["country"][0] = "Brazil"

In [34]: df
Out[34]: 
     name country  age (year)  height (cm)
0  Antony  Brazil        32.1          178
1   Chris  France        25.0          175
```

**(?1)** This time we also got a warning message, but
why did we successfully change to `"Brazil"` in `df`?

**(R1)** Let's try to analyze this step by step:
```python
In [35]: # First we convert Brazil back to Brazin

In [36]: df.loc[0, "country"] = "Brazin"

In [37]: df
Out[37]: 
     name country  age (year)  height (cm)
0  Antony  Brazin        32.1          178
1   Chris  France        25.0          175

In [38]: s = df["country"]

In [39]: type(s)
Out[39]: pandas.core.series.Series

In [40]: s._is_view
Out[40]: True

In [41]: s[[0]]._is_view
Out[41]: False

In [42]: s.loc[[0]]._is_view
Out[42]: False

In [43]: s.iloc[[0]]._is_view
Out[43]: False
```

So the warning message was displayed because `s[[0]]` is
a copy. But that **hasn't explained why**
`df` had been successfully modified.

**(?2)** Does it mean that there is no way to extract
sub-series of a `pd.Series` as a view?
