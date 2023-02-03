# The Newline Char `"\n"`
A line ending with a newline character does not mean that we've started the
line next to it. Instead, most files seem to have an `"\n"` character
at the end of it.

```python
In [18]: with open("newlines.txt", "w") as f:
          ...:     s = "a\nb\nc\nd\n"
          ...:     f.write(s)
          ...:

In [19]: !cat newlines.txt
a
b
c
d

In [20]: !wc -l newlines.txt
4 newlines.txt

In [21]: with open("newlines.txt", "w") as f:
          ...:     s = "a\nb\nc\nd"
          ...:     f.write(s)
          ...:

In [22]: !cat newlines.txt
a
b
c
d
In [23]: !wc -l newlines.txt
3 newlines.txt

```
