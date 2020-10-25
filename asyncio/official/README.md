```python
In [1]: import asyncio

In [2]: async def main():
   ...:     print("hello")
   ...:     await asyncio.sleep(1)
   ...:     print("world")
   ...:

In [3]: main()
Out[3]: <coroutine object main at 0x7f59b25e18c0>

In [4]: main
Out[4]: <function __main__.main()>

In [5]: asyncio.run(main)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-5-f9cbe57ef40e> in <module>
----> 1 asyncio.run(main)

/usr/local/lib/python3.7/asyncio/runners.py in run(main, debug)
     35
     36     if not coroutines.iscoroutine(main):
---> 37         raise ValueError("a coroutine was expected, got {!r}".format(main))
     38
     39     loop = events.new_event_loop()

ValueError: a coroutine was expected, got <function main at 0x7f59b25867a0>

In [6]: asyncio.run(main())
hello
world

In [7]: %time asyncio.run(main())
hello
world
CPU times: user 2.73 ms, sys: 98 µs, total: 2.83 ms
Wall time: 1 s

In [8]: import time

In [9]: t0 = time.time(); asyncio.run(main()); t1 = time.time(); print(f"{t1-t0} s elapsed")
hello
world
1.0041894912719727 s elapsed

In [10]: t0 = time.time(); asyncio.run(main()); t1 = time.time(); print(f"{t1-t0} s elapsed")
hello
world
1.003861427307129 s elapsed

In [11]: t0 = time.time(); asyncio.run(main()); t1 = time.time(); print(f"{t1-t0} s elapsed")
hello
world
1.003835678100586 s elapsed

In [12]: import asyncio
    ...: import time
    ...:
    ...: async def say_after(delay, what):
    ...:     await asyncio.sleep(delay)
    ...:     print(what)
    ...:
    ...: async def main():
    ...:     print(f"started at {time.strftime('%X')}")
    ...:
    ...:     await say_after(2, 'world')
    ...:     await say_after(1, 'hello')
    ...:
    ...:     print(f"finished at {time.strftime('%X')}")
    ...:
    ...: asyncio.run(main())
    ...:
started at 13:50:35
world
hello
finished at 13:50:38

In [13]: import asyncio                                                                                           [25/118]
    ...: import time
    ...:
    ...: async def say_after(delay, what):
    ...:     await asyncio.sleep(delay)
    ...:     print(what)
    ...:
    ...: async def main():
    ...:     print(f"started at {time.strftime('%X')}")
    ...:
    ...:     await say_after(2, 'world')
    ...:     await say_after(1, 'hello')
    ...:
    ...:     print(f"finished at {time.strftime('%X')}")
    ...:
    ...: asyncio.run(main())
    ...:
started at 13:50:58
world
hello
finished at 13:51:01

In [14]: # The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.

In [15]: async def main():
    ...:     taskA = asyncio.create_task(
    ...:         say_after(2, 'world'))
    ...:
    ...:     taskB = asyncio.create_task(
    ...:         say_after(1, 'hello'))
    ...:
    ...:     print(f"started at {time.strftime('%X')}")
    ...:
    ...:     # Wait until both tasks are completed (should take
    ...:     # around 2 seconds.)
    ...:     await taskA
    ...:     await taskB
    ...:
    ...:     print(f"finished at {time.strftime('%X')}")
    ...:

In [16]: asyncio.run(main())
started at 13:53:13
hello
world
finished at 13:53:15

In [17]:


```
