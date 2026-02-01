```python
In [1]: dt.datetime.now()
Out[1]: datetime.datetime(2025, 7, 7, 17, 55, 44, 370281)

In [2]: dt.datetime.now(tz=dt.timezone.utc)
Out[2]: datetime.datetime(2025, 7, 7, 9, 56, 1, 302230, tzinfo=datetime.timezone.utc)

In [3]: dt.datetime.now(tz=dt.timezone.max)
Out[3]: datetime.datetime(2025, 7, 8, 9, 55, 18, 647784, tzinfo=datetime.timezone(datetime.timedelta(seconds=86340)))

In [4]: dt.datetime.now(tz=dt.timezone.min)
Out[4]: datetime.datetime(2025, 7, 6, 9, 57, 29, 612009, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=60)))

In [5]: dt.timezone.max
Out[5]: datetime.timezone(datetime.timedelta(seconds=86340))

In [6]: dt.timezone.min
Out[6]: datetime.timezone(datetime.timedelta(days=-1, seconds=60))

In [7]:
```
