
class Shape:
    def __init__(self, points, order):
        assert len(points) == len(order)
        self._points = points
        self._order = order

    def _get_chain(self):
        arr = []
        for i in range(len(self._order)):
            arr.append(self._points[i])
        return arr

    def perimeter(self):
        arr = self._get_chain()
        N = len(arr)
        perimeter = 0
        for i in range(N):
            perimeter += ((arr[i][0] - arr[(i+1) % N][0])**2 + (arr[i][1] - arr[(i+1) % N][1])**2) ** .5
        return perimeter

    def area(self):
        arr = self._get_chain()
        N = len(arr)
        area = 0
        for i in range(N):
            area += (arr[i][0] - arr[(i+1) % N][0]) * (arr[i][1] + arr[(i+1) % N][1]) / 2
        return abs(area)

    def volume(self, height):
        return self.area() * height / 3


class Hexagon(Shape):
    def __init__(self, id,
                 p1, p2, p3, p4, p5, p6, order):
        self.id = id
        super().__init__([p1, p2, p3, p4, p5, p6], order)


class Octagon(Shape):
    def __init__(self, id,
                 p1, p2, p3, p4, p5, p6, p7, p8, order):
        self._id = id
        super().__init__([p1, p2, p3, p4, p5, p6, p7, p8], order)

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id


if __name__ == '__main__':
    h = Hexagon("hex1", [0, 1], [0, 2], [1, 3], [2, 2], [2, 1], [1, 0], [5, 4, 3, 2, 1, 0])
    print(h.id)
    h.id = "hex2"
    print(h.id)
    print(h.area())
    print(h.perimeter())
    print(h.volume(10))
    o = Octagon("oct1", [0, 1], [0, 2], [1, 3], [2, 3], [3, 2], [3, 1], [2, 0], [1, 0], [0, 1, 2, 3, 4, 5, 6, 7])
    print(o.get_id())
    o.set_id("oct2")
    print(o.get_id())
    print(o.area())
    print(o.perimeter())
    print(o.volume(10))
