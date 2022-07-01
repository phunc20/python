In Linux's `man ln`, the syntax for creating a link is roughly
```bash
# hard link
ln TARGET LINK_NAME
# symbolic link
ln -s TARGET LINK_NAME
```

where `TARGET` refers to the file being linked to and `LINK_NAME` refers to the file linking to the existing `TARGET`.

Put in another way, there must first exists a `TARGET` and only then could we create a `LINK_NAME`

Okay, once we agree on the terms, it'll be easier to explain the usage of the method `symlink_to()`.

For example, say, you have an image under the path `~/pictures/iceberg.jpg` and you want to create
a symbolic link to it under `~/corbeille/ice.jpg` using Python. Here is one way to do it:
```python
from pathlib import Path

target = Path.home() / "pictures/iceberg.jpg"
link = Path.home() / "corbeille/ice.jpg"

link.symlink_to(target)
```

**N.B.** Do pay special attention to relative path and absolute path; the method `path.absolute()` might come in handy from
time to time.
