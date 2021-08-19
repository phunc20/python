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
        return f"{self.name}: ({self.x}, {self.y})"

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

    #def __radd__(self, another):
    #    """
    #    __radd__ probably stands for "Reduce Add".

    #    To be able to use e.g. sum([V1, V2, V3]), one need to implement
    #    this method.
    #    """
    #    return another + self

    def __mul__(self, another):
        if isinstance(another, float) or isinstance(another, int):
            return Vertex(
                another*self.x,
                another*self.y,
                f"({another}){self.name}"
            )

    def __rmul__(self, another):
        return self * another
