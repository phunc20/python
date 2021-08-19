#from ..__lt__.vector import Coord, Vertex
#from ..__lt__ import vector
from vector import Coord, Vertex

if __name__ == "__main__":
    P = Vertex(30, 100, "P")
    Q = Vertex(40, 101, "Q")
    R = Vertex(28, 700, "R")
    S = Vertex(39, 698, "S")
    all_vertices = [P, Q, R, S]
    for vertex in all_vertices:
        print(vertex)
    print(f"P + Q = {P + Q}")
    print(f"R + S = {R + S}")
    print(f"P*3.14 = {P * 3.14}")
    print(f"S * (-7) = {S * (-7)}")
    print(f"3.14*P = {3.14*P}")
    print(f"-7*S = {-7*S}")
    #print(f"sum(all_vertices) = {sum(all_vertices)}")
