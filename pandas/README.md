
## Rename The Columns/Rows
- Use the `rename` method. Note that by default it creates a new DataFrame instead of modifying in-place.
  ```python
  df.rename(columns={
      "old_col_name1": "new_col_name1"
      "old_col_name2": "new_col_name2"
      "old_col_name3": "new_col_name3"
  })
  ```


## `df.describe()`
This method allows us to quickly inspect

- mean
- std
- quartiles
- min, max
- etc.

of the numerical columns of `df`.

**Caveat.** It happens when this method does not print out
the above-mentioned (i.e. mean, quartiles, min, max, etc.).
```
In [16]: df.describe()
Out[16]:
        height  weight
count        4       4
unique       4       4
top        169      65
freq         1       1
```
Normally, it is because of the `dtype` of the columns of your
dataframe. The `dtype` has to be sth like `int8, float32, float64, etc.`
in order for those numerical stats to be properly calculated and shown.

The following is an example:

- bad practice
  ```python
  In [4]: df = pd.DataFrame(index=["alice", "bob", "charlie", "daniel"], columns=["height", "weight"]); df
  Out[4]:
          height weight
  alice      NaN    NaN
  bob        NaN    NaN
  charlie    NaN    NaN
  daniel     NaN    NaN
  
  In [5]: df.dtypes
  Out[17]:
  height    object
  weight    object
  dtype: object
  
  In [7]: random.seed(42)
  
  In [13]: for i in range(len(df)):
      ...:     df.iloc[i] = random.randint(155, 200), random.randint(50, 100)
  
  In [14]: df
  Out[14]:
          height weight
  alice      172     65
  bob        169     58
  charlie    161     93
  daniel     189     55
  
  In [16]: df.describe()
  Out[16]:
          height  weight
  count        4       4
  unique       4       4
  top        169      65
  freq         1       1
  
  In [15]: df.dtypes
  Out[15]:
  height    object
  weight    object
  dtype: object
  ```
  - As shown in our code, we think that the cause is that `pd.DataFrame()` defaults the `dtypes` of its element to `object` if we create an empty data frame.
  
    When we assign a list of values to the rows of the data frame, the data frame simply continues to use the default data type.

- good practice
  ```python
  In [40]: df = pd.DataFrame(index=["alice", "bob", "charlie", "daniel"], columns=["height", "weight"], dtype=np.float32); df.dtypes
  Out[40]:
  height    float32
  weight    float32
  dtype: object
  
  In [41]: for i in range(len(df)):
      ...:     df.iloc[i] = random.randint(155, 200), random.randint(50, 100)
      ...:
  
  In [42]: df
  Out[42]:
           height  weight
  alice     192.0    77.0
  bob       157.0    51.0
  charlie   160.0    63.0
  daniel    169.0    82.0
  
  In [43]: df.describe()
  Out[43]:
            height    weight
  count    4.00000   4.00000
  mean   169.50000  68.25000
  std     15.84375  14.03125
  min    157.00000  51.00000
  25%    159.25000  60.00000
  50%    164.50000  70.00000
  75%    174.75000  78.25000
  max    192.00000  82.00000
  
  In [44]: df.dtypes
  Out[44]:
  height    float16
  weight    float16
  dtype: object

  ```
  - Just as we suspected, changing the input arg `dtype=np.float32` of `pd.DataFrame()` helps specify the data type and everything works well from that point on.
    **N.B.** It seems that only a few of `np`'s data type is specifyable, not all:
    ```python
    In [36]: df = pd.DataFrame(index=["alice", "bob", "charlie", "daniel"], columns=["height", "weight"], dtype=np.uint8); df.dtypes
    Out[36]:
    height    float64
    weight    float64
    dtype: object
    
    In [37]: df = pd.DataFrame(index=["alice", "bob", "charlie", "daniel"], columns=["height", "weight"], dtype=np.int32); df.dtypes
    Out[37]:
    height    float64
    weight    float64
    dtype: object
    
    In [38]: df = pd.DataFrame(index=["alice", "bob", "charlie", "daniel"], columns=["height", "weight"], dtype=np.float16); df.dtypes
    Out[38]:
    height    float16
    weight    float16
    dtype: object
    
    In [39]: df = pd.DataFrame(index=["alice", "bob", "charlie", "daniel"], columns=["height", "weight"], dtype=np.float32); df.dtypes
    Out[39]:
    height    float32
    weight    float32
    dtype: object
    ```
