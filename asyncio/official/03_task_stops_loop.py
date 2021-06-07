import asyncio

async def say_after(what, n_sec):
    await asyncio.sleep(n_sec)
    print(what)

async def stop_after(loop, n_sec):
    await asyncio.sleep(n_sec)
    loop.stop()


loop = asyncio.get_event_loop()

loop.create_task(say_after("1st hello", 2))
loop.create_task(say_after("2nd hello", 1))
loop.create_task(say_after("3rd hello", 4))
loop.create_task(stop_after(loop, 3))

loop.run_forever()
loop.close()
