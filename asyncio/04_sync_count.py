import asyncio

#async def count():
#    print("One")
#    await asyncio.sleep(1)
#    print("Two")
#
#async def main():
#    await asyncio.gather(count(), count(), count())

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()


if __name__ == "__main__":
    import time
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:.2f} seconds.")
