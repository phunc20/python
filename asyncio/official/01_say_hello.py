import asyncio

async def say_after(what, n_sec):
    await asyncio.sleep(n_sec)
    print(what)

loop = asyncio.get_event_loop()
loop.run_until_complete(say_after("hello world", 1))
loop.close()
