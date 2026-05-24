
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Координаты точки: ({self._x}, {self._y})"

    def perimeter(self, other):
        return 2 * (abs(self._x - other.getX()) + abs(self._y - other.getY()))

    def area(self, other):
        return abs(self._x - other.getX()) * abs(self._y - other.getY())

    def getX(self):
        return self._x

    def getY(self):
        return self._y


if __name__ == "__main__":
    p1 = Point(10, 10)
    print(p1)
    p2 = Point(20, 30)
    print(p2)
    print(f'perimeter: {p2.perimeter(p1)}')
    print(f'area: {p1.area(p2)}')
