class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2
square1 = Square(5)
shape2 = Shape()
print(square1.area())
print(shape2.area())
