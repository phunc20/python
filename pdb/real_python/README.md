## Demo
I have designed an example to run Python debugger. Note that `breakpoint()` is a new functionality since Python3.7.

- When `determinant` equals `2`:
  ```bash
  (oft) ~/.../python/pdb/real_python$ python main.py
  Python version = 3.7.10
  > /home/phunc20/git-repos/phunc20/python/pdb/real_python/main.py(10)<module>()
  -> determinant = random.randint(1,2)
  (Pdb) list
  5     if __name__ == "__main__":
  6         python_version = sys.version.split(" ")[0]
  7         print(f"Python version = {python_version}")
  8         breakpt = breakpoint if python_version >= "3.7" else pdb.set_trace
  9         breakpt()
  10  ->     determinant = random.randint(1,2)
  11         if determinant == 1:
  12             breakpt()
  13             from utils import random_2D_coordinates, argsort
  14         else:
  15             breakpt()
  (Pdb) determinant
  *** NameError: name 'determinant' is not defined
  (Pdb) breakpt
  <built-in function breakpoint>
  (Pdb) help(breakpt)
  *** No help for '(breakpt)'
  (Pdb) breakpt == pdb.set_trace
  False
  (Pdb) breakpt == breakpoint
  True
  (Pdb) help
  
  Documented commands (type help <topic>):
  ========================================
  EOF    c          d        h         list      q        rv       undisplay
  a      cl         debug    help      ll        quit     s        unt
  alias  clear      disable  ignore    longlist  r        source   until
  args   commands   display  interact  n         restart  step     up
  b      condition  down     j         next      return   tbreak   w
  break  cont       enable   jump      p         retval   u        whatis
  bt     continue   exit     l         pp        run      unalias  where
  
  Miscellaneous help topics:
  ==========================
  exec  pdb
  
  (Pdb) c
  > /home/phunc20/git-repos/phunc20/python/pdb/real_python/main.py(16)<module>()
  -> from utils2 import random_2D_coordinates, argsort
  --KeyboardInterrupt--
  (Pdb) determinant
  2
  (Pdb) list
  11         if determinant == 1:
  12             breakpt()
  13             from utils import random_2D_coordinates, argsort
  14         else:
  15             breakpt()
  16  ->         from utils2 import random_2D_coordinates, argsort
  17         T_coordinates = random_2D_coordinates(n=7)
  18         print(f"T_coordinates = {T_coordinates}")
  19         argsort(T_coordinates)
  [EOF]
  (Pdb) continue
  T_coordinates = [[27 18]
  [75 15]
  [17 30]
  [65 52]
  [41 59]
  [76 27]
  [65 78]]
  > /home/phunc20/git-repos/phunc20/python/pdb/real_python/utils2.py(17)argsort()
  -> return sorted(range(len(seq)), key=seq.__getitem__)
  (Pdb) list
  12
  13         return
  14             similar result value to np.argsort, just more general-purposed
  15         """
  16         breakpoint()
  17  ->     return sorted(range(len(seq)), key=seq.__getitem__)
  [EOF]
  (Pdb) seq
  array([[27, 18],
  [75, 15],
  [17, 30],
  [65, 52],
  [41, 59],
  [76, 27],
  [65, 78]])
  (Pdb) type(seq)
  <class 'numpy.ndarray'>
  (Pdb) q
  Traceback (most recent call last):
    File "main.py", line 16, in <module>
      from utils2 import random_2D_coordinates, argsort
    File "/home/phunc20/git-repos/phunc20/python/pdb/real_python/utils2.py", line 17, in argsort
      return sorted(range(len(seq)), key=seq.__getitem__)
    File "/home/phunc20/git-repos/phunc20/python/pdb/real_python/utils2.py", line 17, in argsort
      return sorted(range(len(seq)), key=seq.__getitem__)
    File "/home/phunc20/.local/bin/miniconda3/envs/oft/lib/python3.7/bdb.py", line 88, in trace_dispatch
      return self.dispatch_line(frame)
    File "/home/phunc20/.local/bin/miniconda3/envs/oft/lib/python3.7/bdb.py", line 113, in dispatch_line
      if self.quitting: raise BdbQuit
  bdb.BdbQuit
  (oft) ~/.../python/pdb/real_python$ python main.py
  ```
- When `determinant` equals `1`:
  ```bash
  (oft) ~/.../python/pdb/real_python$ python main.py
  Python version = 3.7.10
  > /home/phunc20/git-repos/phunc20/python/pdb/real_python/main.py(10)<module>()
  -> determinant = random.randint(1,2)
  (Pdb) c
  > /home/phunc20/git-repos/phunc20/python/pdb/real_python/main.py(13)<module>()
  -> from utils import random_2D_coordinates, argsort
  (Pdb) determinant
  1
  (Pdb) list
    8         breakpt = breakpoint if python_version >= "3.7" else pdb.set_trace
    9         breakpt()
   10         determinant = random.randint(1,2)
   11         if determinant == 1:
   12             breakpt()
   13  ->         from utils import random_2D_coordinates, argsort
   14         else:
   15             breakpt()
   16             from utils2 import random_2D_coordinates, argsort
   17         T_coordinates = random_2D_coordinates(n=7)
   18         print(f"T_coordinates = {T_coordinates}")
  (Pdb) help(random_2D_coordinates)
  *** No help for '(random_2D_coordinates)'
  (Pdb) c
  T_coordinates = [(46, 19), (31, 72), (96, 30), (62, 16), (37, 55), (85, 10), (74, 12)]
  > /home/phunc20/git-repos/phunc20/python/pdb/real_python/utils.py(18)argsort()
  -> return sorted(range(len(seq)), key=seq.__getitem__)
  (Pdb) random_2D_coordinates.__file__
  *** AttributeError: 'function' object has no attribute '__file__'
  (Pdb) list
   13
   14         return
   15             similar result value to np.argsort, just more general-purposed
   16         """
   17         pdb.set_trace()
   18  ->     return sorted(range(len(seq)), key=seq.__getitem__)
  [EOF]
  (Pdb) type(seq)
  <class 'list'>
  (Pdb) seq
  [(46, 19), (31, 72), (96, 30), (62, 16), (37, 55), (85, 10), (74, 12)]
  (Pdb) c
  (oft) ~/.../python/pdb/real_python$
  ```
- When running the script with **`python -m pdb main.py`**:
  ```bash
  (oft) ~/.../python/pdb/real_python$ python -m pdb main.py
  > /home/phunc20/git-repos/phunc20/python/pdb/real_python/main.py(1)<module>()
  -> import random
  (Pdb) n
  > /home/phunc20/git-repos/phunc20/python/pdb/real_python/main.py(2)<module>()
  -> import pdb
  (Pdb) n
  > /home/phunc20/git-repos/phunc20/python/pdb/real_python/main.py(3)<module>()
  -> import sys
  (Pdb) n
  > /home/phunc20/git-repos/phunc20/python/pdb/real_python/main.py(5)<module>()
  -> if __name__ == "__main__":
  (Pdb) n
  > /home/phunc20/git-repos/phunc20/python/pdb/real_python/main.py(6)<module>()
  -> python_version = sys.version.split(" ")[0]
  (Pdb) q
  (oft) ~/.../python/pdb/real_python$
  ```
