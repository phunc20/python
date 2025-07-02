

Install packages in a virtual environment in `uv`:

- Don't `uv pip install`; instead, `uv add`
- For one-off requirements, use `uvx` or `uv run --with`.
- Add the following to your `pyproject.toml` if you don't want `uv`
  to manage the project environment:
  ```
  [tool.uv]
  managed = false
  ```


