## Environment
- Python 3.10.9


## Back Reference
Sometimes you need `re` to capture sth
and place it somewhat differently. This
is when back ref comes in handy.
- Surround the thing to be captured by parentheses, i.e. `r'(sth)'`
- To specify its new location, use, e.g. `\1` to refer to the first captured pattern. (**N.B.** This is 1-indexed instead of 0-indexed)

Please run to better understand how this works.
```bash
$ python sub_sent_joint.py
```

