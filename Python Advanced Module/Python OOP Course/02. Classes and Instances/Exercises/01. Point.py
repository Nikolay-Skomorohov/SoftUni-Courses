import math


class Point:
    def __init__(self, x, y):
        self.x1 = x
        self.y1 = y

    def set_x(self, new_x):
        self.x1 = new_x

    def set_y(self, new_y):
        self.y1 = new_y

    def distance(self, x2, y2):
        result = math.sqrt(((x2 - self.x1) ** 2) + ((y2 - self.y1) ** 2))
        return result


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
