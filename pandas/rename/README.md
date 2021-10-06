### How to rename the columns?
```python
df = pd.DataFrame({
    "File Name": ["a.png", "b.png", "c.png"],
    "Total Dollars": [10, 15, 5],
})
df.rename(columns={
    "File Name": "filename",
    "Total Dollars": "price",
})
```
Note that the `inplace` option is by default `False`.
