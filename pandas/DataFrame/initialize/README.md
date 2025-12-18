With an example entry like the following:

```python
example_entry = {
    'code': 88433,
    'name': '可憐的小姑娘',
    'singer': '郭金發',
    'lang': '台',
}
```

One has different options to initialize a Pandas DataFrame:

1. Specifying `dtype` using `pd.Series` and for-loop
   ```python
   df = pd.DataFrame({
       k: pd.Series(dtype="str")
       if isinstance(v, str) else
       pd.Series(dtype="int64")
       for k, v in example_entry.items()
   })
   ```
1. W/o specifying `dtype` for each column
   ```python
   df = pd.DataFrame(
       columns=('code', 'name', 'singer', 'lang',),
   )
   ```
1. Specifying `dtype` manually
   ```python
   df = pd.DataFrame({
       'code': pd.Series(dtype="int64"),
       'name': pd.Series(dtype="str"),
       'singer': pd.Series(dtype="str"),
       'lang': pd.Series(dtype="str"),
   })
   ```
