import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Grid:
    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
        self.data = [] 

        for row in range(0, depth):
            self.data.append([0] * width)
    
    def draw_line(self, p1, p2):
        xDist = abs(p2.x - p1.x)
        yDist = abs(p2.y - p1.y)

        xDir = 0
        yDir = 0

        if p1.x > p2.x:
            xDir = -1
        elif p1.x < p2.x:
            xDir = 1

        if p1.y > p2.y:
            yDir = -1
        elif p1.y < p2.y:
            yDir = 1

        xIdx = p1.x
        yIdx = p1.y

        while abs(xIdx - p1.x) <= xDist and abs(yIdx - p1.y) <= yDist:
            self.data[yIdx][xIdx] += 1
            xIdx += xDir
            yIdx += yDir


def parse_line(line):
    one, arrow, two = line.split(' ')

    p1 = list(map(int, one.split(',')))
    p2 = list(map(int, two.split(',')))

    p1 = Point(p1[0], p1[1])
    p2 = Point(p2[0], p2[1])

    return Line(p1, p2)
    
def read_input():
    with open(sys.argv[1] ,'r') as file:
        input = file.read().strip().split('\n')
    return input

def locate_vents(input):
    input = read_input()
    lines = list(map(parse_line, input))

    longestRow = 0
    longestCol = 0

    for line in lines:
        if line.p1.y > longestCol:
            longestCol = line.p1.y
        if line.p2.y > longestCol:
            longestCol = line.p2.y
        if line.p1.x > longestRow:
            longestRow = line.p1.x
        if line.p2.x > longestRow:
            longestRow = line.p2.x

    grid = Grid(longestCol + 1, longestRow + 1)

    for line in lines:
        p1 = line.p1
        p2 = line.p2

        grid.draw_line(p1, p2)

    overlaps = 0

    for row in grid.data:
        for cell in row:
            if cell >= 2:
                overlaps += 1
    
    return overlaps


print(f'overlaps: {locate_vents(read_input())}')