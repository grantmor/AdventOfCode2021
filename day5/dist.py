from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 1)
p2 = Point(5, 5)

def distance(p1, p2):
    hypLength = sqrt(pow((p2.y - p1.y), 2) + pow((p2.x - p1.x), 2))
    return hypLength

print(distance(p1, p2))