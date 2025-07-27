## `ruff format`
Will automatically edit your files according to some best practices, so
better version-control your files before running this command and
`git diff` to verify the changes before `git commit` them.


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
