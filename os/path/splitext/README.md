The `help(os.path.splitext)` says
```
splitext(p)
    Split the extension from a pathname.

    Extension is everything from the last dot to the end, ignoring
    leading dots.  Returns "(root, ext)"; ext may be empty.

```

**Rmk.** `splitext()`
- is **not** `split + text`
- is `split + ext`, i.e. split extension.

Here are some examples which might help better grasp the way it is used.<br>
**Note** how **the leading dot** of a hidden folder/file is **ignored**.
```ipython
In [5]: path1 = "/home/phunc20/.useful-scripts/ju-pwd-url"

In [6]: os.path.splitext(path1)
Out[6]: ('/home/phunc20/.useful-scripts/ju-pwd-url', '')

In [7]: path2 = "/home/phunc20/.useful-scripts/code-copy.sh"

In [8]: os.path.splitext(path2)
Out[8]: ('/home/phunc20/.useful-scripts/code-copy', '.sh')

In [9]: os.path.splitext("/home/phunc20/.bashrc")
Out[9]: ('/home/phunc20/.bashrc', '')

In [10]:
```
