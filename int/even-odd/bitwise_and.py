import argparse
import random
import time

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num", type=int, default=1_000_000, help="The number of integers you want to test.")
ap.add_argument("-c", "--ceil", type=int, default=1_000_000_000_000, help="The ceilling no integer whose parity you want to test will be gt.")
args = ap.parse_args()

def is_odd(n):
    """
    1 in binary is 00...01, so using "bitwise and" (n & 1) we are able to check
    whether the smallest bit of n is 1 or 0, and deduce the parity of n.

    args:
        n, int

    return:
        int, 0 or 1. 0 means False, 1 means True, as usual.
    """
    return n & 1



if __name__ == "__main__":
    # Test01
    t0 = time.time()
    for i in range(args.num):
        is_odd(i)
    t1 = time.time()
    print(f"Test01 took {t1 - t0} (sec)")

    # Test02
    random.seed(42)
    t2 = time.time()
    for i in range(args.num):
        #is_odd(random.randint(0, args.ceil))
        is_odd(random.randint(args.ceil, 2*args.ceil))
    t3 = time.time()
    print(f"Test02 took {t3 - t2} (sec)")
