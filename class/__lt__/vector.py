class Coord():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self):
        return self.name

class Vertex():
    proximity_px = 3
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
    
    def __repr__(self):
        return self.name

    def __lt__(self, another):
        diff_y = another.y - self.y
        if  diff_y > Vertex.proximity_px:
            return True
        elif -diff_y > Vertex.proximity_px:
            return False
        else:
            diff_x = another.x - self.x
            return diff_x > Vertex.proximity_px

    def __add__(self, another):
        return Vertex(
            self.x + another.x,
            self.y + another.y,
            f"{self.name} + {another.name}",
        )

if __name__ == "__main__":
    A = Coord(30, 100, "A")
    B = Coord(40, 101, "B")
    C = Coord(28, 700, "C")
    D = Coord(39, 698, "D")
    try:
        print(f"sorted([B, D, A, C]) = {sorted([B, D, A, C])}")
    except TypeError as e:
        print("---> print(sorted([B, D, A, C]))")
        print(f"TypeError: {e}")

    print()
    a = (A.x, A.y)
    b = (B.x, B.y)
    c = (C.x, C.y)
    d = (D.x, D.y)
    L = [a, b, c, d]
    print("sorted(\"bdac\", key=lambda char: L[ord(char) - ord('a')]) = ", end='')
    print(sorted("bdac", key=lambda char: L[ord(char) - ord('a')][::-1]))

    print()
    P = Vertex(30, 100, "P")
    Q = Vertex(40, 101, "Q")
    R = Vertex(28, 700, "R")
    S = Vertex(39, 698, "S")
    try:
        print(f"sorted([Q, S, P, R]) = {sorted([Q, S, P, R])}")
    except TypeError as e:
        print("---> print(sorted([Q, S, P, R]))")
        print(f"TypeError: {e}")
