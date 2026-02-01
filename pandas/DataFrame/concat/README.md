```
pd.conat(
    (pd.read_csv() for f in folder.glob("*.csv")),
    index=False,
)
```
