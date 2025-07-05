## `.jsonl`
Here is how to save a Pandas DataFrame into `.jsonl` format

```python
df.to_json("/tmp/lullaby.jsonl", orient="records", lines=True)
```

i.e. specify two options

1. `orient="records"`
2. `lines=True`
