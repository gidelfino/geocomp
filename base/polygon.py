from point import Point

class PolygonIterator:
    def __init__(self, polygon):
        self.N = polygon.N
        self.head = polygon.head
        self.cur = 0

    def __next__(self):
        if self.cur < self.N:
            self.cur += 1
            self.head = self.head.next
            return self.head.prev
        else:
            raise StopIteration()

class Polygon:
    """ Pontos estao na direcao anti-horaria """
    """ Implementado com lista ligada """

    def __init__ (self, points):
        """ Points eh uma lista de Point """
        self.head = points[0]
        self.N = len(points)

        cur = self.head
        for i in range(1, len(points)):
            cur.next = points[i]
            cur.next.prev = cur
            cur = cur.next

        cur.next = self.head
        self.head.prev = cur

    def __iter__(self):
        return PolygonIterator(self)

    def __str__(self):
        return ', '.join([str(p) for p in self])


a = Point(0, 0)
b = Point(1, 1)
c = Point(2, 2)
d = Point(3, 3)

p = Polygon([a, b, d, c])
print(p)
