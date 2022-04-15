

## Useful Ones
- post-mortem (死後): Sometimes you may want to debug and know the values of a few variables, **after** your
  program breaks. A convenient way to do this is, say, the script you want to get executed being named `eval.py`,
  ```bash
  python -m ipdb eval.py
  ```
- `pp` pretty print. Note how long lists get more organized printing when using `pp`.
  ```python
  (Pdb) pp os.path.sys.path
  ['/home/phunc20/git-repos/phunc20/python/pdb/real_python/nathan_jennings',
   '/home/phunc20/.config/miniconda3/envs/oft/lib/python37.zip',
   '/home/phunc20/.config/miniconda3/envs/oft/lib/python3.7',
   '/home/phunc20/.config/miniconda3/envs/oft/lib/python3.7/lib-dynload',
   '/home/phunc20/.local/lib/python3.7/site-packages',
   '/home/phunc20/.config/miniconda3/envs/oft/lib/python3.7/site-packages']
  (Pdb) p os.path.sys.path
  ['/home/phunc20/git-repos/phunc20/python/pdb/real_python/nathan_jennings', '/home/phunc20/.config/miniconda3/envs/oft/lib/python37.zip', '/home/phunc20/.config/miniconda3/envs/oft/lib/python3.7', '/home/phunc20/.config/miniconda3/envs/oft/lib/python3.7/lib-dynload', '/home/phunc20/.local/lib/python3.7/site-packages', '/home/phunc20/.config/miniconda3/envs/oft/lib/python3.7/site-packages']
  ```




