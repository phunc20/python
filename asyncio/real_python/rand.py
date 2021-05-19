import asyncio
import random

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

async def make_random(idx: int, threshold: int = 6) -> int:
    print(f"{c[idx + 1]}Initiated make_random({idx})")
    # Recall that random.randint(a, b) includes both ends, i.e. [a, b]
    i = random.randint(0, 10)
    while i <= threshold:
        print(f"{c[idx + 1]}make_random({idx}) equals {i}: Too low. Retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(f"{c[idx + 1]}---> Finished: make_random({idx}) equals {i}{c[0]}")
    return i

async def main():
    res = await asyncio.gather(
        *(make_random(i, 10-i-1) for i in range(3))
    )
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1 equals {r1}")
    print(f"r2 equals {r2}")
    print(f"r3 equals {r3}")
