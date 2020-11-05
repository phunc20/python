
<pre>
[phunc20@artichaut-x220 asyncio]$ python 01_async_count.py
One
One
One
Two
Two
Two
01_async_count.py executed in 1.00 seconds.
[phunc20@artichaut-x220 asyncio]$ python 02_async_count.py
Traceback (most recent call last):
  File "02_async_count.py", line 15, in <module>
    asyncio.run(main())
  File "/usr/lib/python3.8/asyncio/runners.py", line 43, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete
    return future.result()
  File "02_async_count.py", line 10, in main
    await asyncio.gather(count, count, count)
  File "/usr/lib/python3.8/asyncio/tasks.py", line 806, in gather
    fut = ensure_future(arg, loop=loop)
  File "/usr/lib/python3.8/asyncio/tasks.py", line 673, in ensure_future
    raise TypeError('An asyncio.Future, a coroutine or an awaitable is '
TypeError: An asyncio.Future, a coroutine or an awaitable is required
</pre>
