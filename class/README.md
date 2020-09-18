

In [28]: class Chocolate:
    ...:     price = 40
    ...:     def __init__(self, brand="mNm's"):
    ...:         self.brand = brand
    ...:
    ...:

In [29]: c = Chocolate()

In [30]: c.price
Out[30]: 40

In [31]: class Chocolate:
    ...:     price = 40
    ...:     def __init__(self, brand="mNm's"):
    ...:         self.brand = brand
    ...:         print(f"self.price = {self.price}")
    ...:
    ...:
    ...:

In [32]: c = Chocolate()
self.price = 40
