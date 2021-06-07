import asyncio
import time

async def count():
    print("One")
    await time.sleep(1)
    print("Two")

async def main():
    ## TypeError: object NoneType can't be used in 'await' expression
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:.2f} seconds.")
