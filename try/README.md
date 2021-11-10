## Frequently used pattern
```python
try:
    do_sth()
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")
```










