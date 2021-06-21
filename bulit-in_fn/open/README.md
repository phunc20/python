## Open Image Files
- must use `"rb"` (for "read" and "binary") instead of simply `"r"`
  - `"br"` is ok, too. (i.e. The order does not matter.)

```
In [47]: path_imagefile = Path("/home/phunc20/datasets/t-brain/chinese_handwrite/train/48705_裕.jpg")

In [48]: path_textfile = Path("/home/phunc20/vol.md")

In [49]: with open(path_imagefile, "r") as f:
    ...:     content = f.read()
    ...:
    ...:
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-49-467006bdf8e4> in <module>
      1 with open(path_imagefile, "r") as f:
----> 2     content = f.read()
      3
      4

~/.config/miniconda3/envs/oft/lib/python3.7/codecs.py in decode(self, input, final)
    320         # decode input (taking the buffer into account)
    321         data = self.buffer + input
--> 322         (result, consumed) = self._buffer_decode(data, self.errors, final)
    323         # keep undecoded input until the next call
    324         self.buffer = data[consumed:]

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

In [50]: with open(path_imagefile, "rb") as f:
    ...:     content = f.read()
    ...:

In [51]: content
Out[51]: b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06...'

In [56]: type(content)
Out[56]: bytes

In [52]: with open(path_textfile, "r") as f:
    ...:     content = f.read()
    ...:

In [53]: content
Out[53]: '4.0K\tanimal.sql\n4.0K\tDownloads\n4.0K\tsd-card\n8.0K\tDesktop\n12K\tArduino\n56K\thw2.jl\n364K\tscikit_learn_data\n596K\ttodo\n648K\tbrowser-tabs\n11M\tgo\n27M\tpictures\n79M\tmusic\n457M\tjobs\n1.8G\tcorbeille\n2.5G\tbiblio\n6.6G\tgit-repos\n7.6G\tcell-phones\n21G\tdatasets\n24G\tmooc\n38G\tdownloads\n207G\tvideos\n'

In [56]: type(content)
Out[56]: str

In [54]: with open(path_textfile, "br") as f:
    ...:     content = f.read()

In [55]: content
Out[55]: b'4.0K\tanimal.sql\n4.0K\tDownloads\n4.0K\tsd-card\n8.0K\tDesktop\n12K\tArduino\n56K\thw2.jl\n364K\tscikit_learn_data\n596K\ttodo\n648K\tbrowser-tabs\n11M\tgo\n27M\tpictures\n79M\tmusic\n457M\tjobs\n1.8G\tcorbeille\n2.5G\tbiblio\n6.6G\tgit-repos\n7.6G\tcell-phones\n21G\tdatasets\n24G\tmooc\n38G\tdownloads\n207G\tvideos\n'

In [56]: type(content)
Out[56]: bytes
```



