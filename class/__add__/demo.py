#from ..__lt__.vector import Coord, Point
#from ..__lt__ import vector
from vector import Coord, Point

if __name__ == "__main__":
    P = Point(30, 100, "P")
    Q = Point(40, 101, "Q")
    R = Point(28, 700, "R")
    S = Point(39, 698, "S")
    all_pts = [P, Q, R, S]
    for pt in all_pts:
        print(pt)
    print(f"P + Q = {P + Q}")
    print(f"R + S = {R + S}")
    print(f"P*3.14 = {P * 3.14}")
    print(f"S * (-7) = {S * (-7)}")
    print(f"3.14*P = {3.14*P}")
    print(f"-7*S = {-7*S}")
    #print(f"sum(all_pts) = {sum(all_pts)}")
