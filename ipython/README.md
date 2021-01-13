





## Crash at Tab-auto-complete
This happened around mid January 2021, in each newly created virtualenv, when I used `ipython` and wanted to auto-complete any
word, the `ipython` would get crashed.

[Solution](https://stackoverflow.com/questions/65663127/ipython-7-19-0-crash)

Briefly speaking, it says that it was the fault of `jedi==1.18.0` and it sufficed to downgrade to `jedi==0.17.2`
```bash
(homl-1e) ~ ❯❯❯ pip list | grep jedi
jedi                 0.18.0
(homl-1e) ~ ❯❯❯ pip install jedi==0.17.2
```



