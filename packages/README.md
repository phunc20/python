## Where The Package Is Installed from?
Let's take the non-existing package `foo` as an example.
```python
import foo
foo.__path__
```

The `foo.__path__` will show you the path. This is especially useful when the package is installed locally, i.e.
installed by the command `pip install -e`

