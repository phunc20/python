import asyncio

async def say_after(what, n_sec):
    await asyncio.sleep(n_sec)
    print(what)

loop = asyncio.get_event_loop()

loop.create_task(say_after("1st hello", 2))
loop.create_task(say_after("2nd hello", 1))

loop.run_forever()
loop.close()
