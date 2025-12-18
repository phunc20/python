## `ruff format`
Will automatically edit your files according to some best practices, so
better version-control your files before running this command and
`git diff` to verify the changes before `git commit` them.

# The Ruff Linter
## `ruff check`
How to have `ruff check` ignore (recursively) some (sub)directories?

- Specify in `pyproject.toml`
  ```toml
  [tool.ruff]
  extend-exclude = ["migrations", "build", "src/.trash"] # Excludes 'migrations', 'build' and 'src/.trash' directories
  ```
    - Single file exclusion and wildcard exclusion are also possible.
      ```toml
      [tool.ruff]
      extend-exclude = ["src/.trash/util.py"]
      ```
      or
      ```toml
      [tool.ruff]
      extend-exclude = ["**/cache/*"]
      ```


## Rule Selection
By default many rules are not applied, e.g. `isort` is not, i.e. the Python
import (alphabetical) order, among other things, is not checked.

If one want some rules, one should include them, say, in `pyproject.toml`.
For instance,

```toml
[tool.ruff.lint]
select = [
    # pycodestyle
    "E",
    # pyflakes
    "F",
    # pyupgrade
    "UP",
    # flake8-bugbear
    "B",
    # flake8-simplify
    "SIM",
    # isort
    "I",
]
```


## Fixes
`ruff check` only indicates the places where some rules are not respected;
to auto-fix these places, run `ruff check --fix`.
