import random
import pdb
import sys

if __name__ == "__main__":
    python_version = sys.version.split(" ")[0]
    print(f"Python version = {python_version}")
    breakpt = breakpoint if python_version >= "3.7" else pdb.set_trace
    breakpt()
    determinant = random.randint(1,2)
    if determinant == 1:
        breakpt()
        from utils import random_2D_coordinates, argsort
    else:
        breakpt()
        from utils2 import random_2D_coordinates, argsort
    T_coordinates = random_2D_coordinates(n=7)
    print(f"T_coordinates = {T_coordinates}")
    argsort(T_coordinates)
