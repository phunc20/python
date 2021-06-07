"""
Does the order of appearance of the coroutines inside gather() matter?
"""
import asyncio

async def print_every_minute():
    "Print min for ten minutes"
    for i in range(1, 10+1):
        await asyncio.sleep(60)
        print(f"\tmin {i:2d}")

async def print_every_second():
    "Print sec for ten minutes"
    for _ in range(10):
        for i in range(1, 60+1):
            print(f"sec {i:2d}")
            await asyncio.sleep(1)

print(f"type(print_every_minute) = {type(print_every_minute)}")
print(f"type(print_every_minute()) = {type(print_every_minute())}")

loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(print_every_second(),
                   print_every_minute())
)
loop.close()

