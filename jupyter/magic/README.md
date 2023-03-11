
## Some Useful Ones
- In order to run Python script(s) from within Jupyter notebooks w/o having to restart the kernel every time
  one modifies the script(s):
  ```python
  %load_ext autoreload
  %autoreload 2
  ```
- `%matplotlib notebook` and `%matplotlib inline`: The latter has actually become jupyter notebook's default since about 2020.
  Their difference is that the former allows _interactive_ plots while the latter _static_ plots.

