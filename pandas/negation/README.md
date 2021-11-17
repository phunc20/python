Negation is achieved by adding `~` before a boolean series:

```python
# say, s is a boolean series
df[~s]
# another example
df[~df["salary"] > 1500]
```
