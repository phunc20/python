With an example entry like the following:

```python
example_entry = {
    'seq': 2908,
    'id': 170479,
    'code': '88433',
    'name': '可憐的小姑娘',
    'singer': '郭金發',
    'lang': '台',
    'sex': '男',
    'company': '弘音',
    'songDate': '114-03',
    'subname': '',
    'songDetailID': '12032',
    'counter': 7497,
    'dateSorter': 11403,
    'len': 6,
    'artistIMG': 'https://i.kfs.io/artist/global/21452,0v1/fit/300x300.jpg',
}
```

One has different options to initialize a Pandas DataFrame:

1. ```python
   df = pd.DataFrame({
       k: pd.Series(dtype="str")
       if isinstance(v, str) else
       pd.Series(dtype="int64")
       for k, v in example_entry.items()
   })
   ```
2. ```python
   df = pd.DataFrame(
       columns=('seq', 'id', 'code', 'name', 'singer',
                'lang', 'sex', 'company', 'songDate',
                'subname', 'songDetailID', 'counter',
                'dateSorter', 'len', 'artistIMG'),
       dtype=(int, int, str, str, str, str, str, str),
   )
   columns = []
   dtype = []
   for k, v in example_entry.items():
       columns.append(k)
       dtype.append(type(v))
   
   df = pd.DataFrame(
       columns=columns,
       dtype=dtype,
   )
   ```
