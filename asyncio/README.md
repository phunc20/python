A coroutine is a specialized version of a Python generator function.

In `asyncio` the generators are called **coroutines**.
The loop to execute them, i.e. coroutines, is the **event loop**



## A Trick on Python REPL (from [Miguel Grinberg](https://www.youtube.com/watch?v=pDnSNYgiQZE&t=75s))
Run **`python -m asyncio`** to start a Python REPL which enables you to `await` outside functions.
- w/o `-m asyncio`
  ```python
  (py3.9) [phunc20@T460p ~]$ python
  Python 3.9.12 (main, Jun  1 2022, 11:38:51)
  [GCC 7.5.0] :: Anaconda, Inc. on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import asyncio
  >>> async def f():
  ...     print("f is running...")
  ...     return 42
  ...
  >>> result = f()
  >>> result
  <coroutine object f at 0x7f23b98ac5c0>
  >>> await result
    File "<stdin>", line 1
  SyntaxError: 'await' outside function
  >>>
  ```
- w/ `-m asyncio`
  ```python
  (py3.9) [phunc20@T460p ~]$ python -m asyncio
  asyncio REPL 3.9.12 (main, Jun  1 2022, 11:38:51)
  [GCC 7.5.0] on linux
  Use "await" directly instead of "asyncio.run()".
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import asyncio
  >>> async def f():
  ...     print("f is running...")
  ...     return 42
  ...
  >>> result = f()
  >>> result
  <coroutine object f at 0x7fee5ddc0640>
  >>> await result
  f is running...
  42
  >>>
  ```
  **Note.** When you specify `-m asyncio`, the first line of `import asyncio` inside the REPL is actually written
  automatically for you.
