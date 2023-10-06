Note that when converted to CSV file,
- `None`, `np.nan`, empty string will all become **nothing**
- Strings will not retain the quotation marks
    - Consequently, for digits, it's hard to know whether they are `str` or `int` from CSV


```python
In [50]: D = {"name": [""], "surname": [None], "height": [np.nan], "weight": "128"}

In [51]: df = pd.DataFrame.from_dict(D)

In [52]: df.to_csv("/tmp/test.csv", index=False)

In [53]: !bat /tmp/test.csv
───────┬────────────────────────────────────────────────────────────────────────
       │ File: /tmp/test.csv
───────┼────────────────────────────────────────────────────────────────────────
   1   │ name,surname,height,weight
   2   │ ,,,128
───────┴────────────────────────────────────────────────────────────────────────

In [54]:
```
