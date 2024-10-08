## IPython Magic
1. `%run <your_script.py>` is the way one runs a Python script form within an IPython session.
1. To automatically have IPython open `matplotlib.pyplot` plots, use the magic `%matplotlib`
1. To display images
   ```python
   from IPython.display import Image
   Image("my_fig.png")
   ```
1. To auto-reload modified library code
   ```python
   %load_ext autoreload
   %autoreload 2
   ```


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

## Using Vim in IPython?
```python
~/.ipython/profile_default/ipython_config.py
----
#c.TerminalInteractiveShell.editing_mode = 'vi'
```
- Enable: Find and uncomment the above line
- Disable: Find and comment the above line


## History
- `%history ~1/` prints historical code from one session before
- `%history ~11/1-10` prints historical code line 1 to 10 from 11 session before
- `%history -f filename.txt` save the current session into `filename.txt`
