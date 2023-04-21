
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


## From inside `ipdb`
- `j` or `jump`: You can jump forward and backward to examine code in the "past" or in the "future".
- Breakpoint or temporary breakpoint
    - Temporary breakpoints will serve for one time and removed automatically
    - Specify absolute Python script path, e.g.
      ```python
      ipdb> tbreak /home/phunc20/projects/pixelize_passport/util.py:726
      ```
    - Specify only line number: Presumably referring to the current file, i.e. where `ipdb` now locates




