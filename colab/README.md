

## Use Colab along with Your Google Drive
Colab provides some convenience class for mounting your Google Drive
onto the machine running your Colab session. Here is how:
```python
from google.colab import drive
path_mount = "/content/google_drive"
drive.mount(path_mount)
```

**Rmk.**

- `path_mount` can be any path you find convenient. Normally, you should by default find yourself under the
  path `/content` when you open a Colab session.
- The `drive.mount()` will prompt you to **Enter your authorization code**. This is only for security sake.
  Just follow the google link and obtain the authorization code to allow Colab to mount your Google Drive in order
  to use it.


In addition, if there is a directory of Python code which you want to use, it might interest you to add that path
to Python's knowledge:
```python
import sys
sys.path.append("/content/google_drive/my_super_cool_python_code_repo")
```



