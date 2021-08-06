## [stackoverflow](https://stackoverflow.com/questions/39092067/pandas-dataframe-convert-column-type-to-string-or-categorical)
With `pandas >= 1.0` there is now a dedicated string datatype:
1) You can convert your column to this pandas string datatype using `.astype('string')`: `df['zipcode'] = df['zipcode'].astype('string')`
2) This is different from using `str`, which sets to the pandas `object` datatype: `df['zipcode'] = df['zipcode'].astype(str)`

One scenario for this is that

- When using the Python package `datasets` and wanting to put a Pandas dataframe `df`
  containing columns of `Path` object into `Dataset.from_pandas(df)`, there will be errors complaining sth like
  ```
  ArrowInvalid: ("Could not convert PosixPath('RVL_CDIP_one_example_per_class/resume/0000157402.tif') with type PosixPath: did not recognize Python value type when inferring an Arrow data type", 'Conversion failed for column image_path with type object')
    ```
- One needs to convert to string datatype:
  ```python
  df["image_path"] = df["image_path"].astype("string")
  ```
