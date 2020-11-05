import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())
    #await asyncio.gather(count, count, count)

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    # The following three prints print out the same thing.
    print(f"{__file__} executed in {elapsed:.2f} seconds.")
    #print(f"{__file__} executed in {elapsed:03.2f} seconds.")
    #print(f"{__file__} executed in {elapsed:0.2f} seconds.")
