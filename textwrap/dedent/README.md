## Example
```
In [1]: import textwrap

In [2]: s = """
    ...:     This line and the next
    ...:     will have their common
    ...:     indentation removed.
    ...: """

In [3]: textwrap.dedent(s)
Out[3]: '\nThis line and the next\nwill have their common\nindentation removed.\n'

In [4]: print(textwrap.dedent(s))

This line and the next
will have their common
indentation removed.


In [5]: s1 = """\
    ...:     This line and the next
    ...:     will have their common
    ...:     indentation removed.
    ...: """

In [6]: print(textwrap.dedent(s1))
This line and the next
will have their common
indentation removed.


In [7]: textwrap.dedent(s1)
Out[7]: 'This line and the next\nwill have their common\nindentation removed.\n'

In [8]: s2 = """\
    ...:     This line and the next
    ...:     will have their common
    ...:     indentation removed.\
    ...: """

In [9]: print(textwrap.dedent(s2))
This line and the next
will have their common
indentation removed.

In [10]: textwrap.dedent(s2)
Out[10]: 'This line and the next\nwill have their common\nindentation removed.'
```
