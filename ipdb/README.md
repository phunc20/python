
- `python -m ipdb my_super_script.py`
- `launch_ipdb_on_exception`
  ```python
  with launch_ipdb_on_exception():
      main()
  ```
- `set_trace`
  ```python
  import ipdb

  ipdb.set_trace()
  suspected_bug_code()
  ```








