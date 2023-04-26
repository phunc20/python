
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
- (Important!) `u` and `d`: Move one level up or down in the stack trace
    - For example, you are deep inside the call stack of some function, and you
      want to examine some variable, which is not in the current local scope but
      in some calling function several levels up, then you can simply `u` until
      you reach that level



