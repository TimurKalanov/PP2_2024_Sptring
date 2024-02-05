import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"coordinates: ({self.x} {self.y})")
    def move(self,dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def dist(self, second_point):
        return math.sqrt( (self.x - second_point.x)**2 + (self.y - second_point.y)**2 )

point1 = Point(3, 4)
point2 = Point(7, 9)

point1.show()

point1.move(2, 3)
point1.show()

print(point1.dist(point2))

