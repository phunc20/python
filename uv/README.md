

Install packages in a virtual environment in `uv`:

- Don't `uv pip install`; instead, `uv add`
- For one-off requirements, use `uvx` or `uv run --with`.
- Add the following to your `pyproject.toml` if you don't want `uv`
  to manage the project environment:
  ```
  [tool.uv]
  managed = false
  ```


## Initialize A Project
- `src` layout (package)
  ```
  $ uv init --package my-project
  $ tree .
  .
  ├── pyproject.toml
  ├── README.md
  ├── src
  │   └── my_project
  │       └── __init__.py
  └── uv.lock
  
  3 directories, 4 files
  ```
- Specify Python version, e.g.
  ```
  $ uv init my-project --python 3.14
  $ grep python my-project/pyproject.toml
  requires-python = ">=3.14"
  ```
