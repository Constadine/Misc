from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def print_point(self):
        print(f"({self.x}, {self.y})")


class Line:
    def __init__(self, point_A=None, point_B=None):
        if point_A is None:
            self.point_A = Point(0, 0)
        else:
            self.point_A = point_A
        if point_B is None:
            self.point_B = Point(0, 0)
        else:
            self.point_B = point_B

    def set_point_A(self, point_A):
        self.point_A = point_A

    def set_point_B(self, point_B):
        self.point_B = point_B

    def length(self):
        return sqrt((self.point_A.x - self.point_B.x)**2 + (self.point_A.y - self.point_B.y)**2)

    def print_line(self):
        self.point_A.print_point()
        self.point_B.print_point()


l = Line()
l.print_line()
print(l)

l.set_point_A(Point(1, 1))
l.set_point_B(Point(4, 5))

l.print_line()
print(l.length())
