
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
    pass
