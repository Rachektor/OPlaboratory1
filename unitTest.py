import unittest
import rectangle
import circle
import square
import triangle
import math


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEquals(rectangle.area(10, 0), 0)
        self.assertEquals(rectangle.area(5, 5), 25)
        self.assertEquals(rectangle.area(100, 1), 100)
        self.assertEquals(rectangle.area(4, 25), 100)
        self.assertEquals(rectangle.area(12, 5), 60)

    def test_perimeter(self):
        self.assertEquals(rectangle.perimeter(3, 5), 16)
        self.assertEquals(rectangle.perimeter(10, 12), 44)
        self.assertEquals(rectangle.perimeter(0, 0), 0)
        self.assertEquals(rectangle.perimeter(5, 6), 22)
        self.assertEquals(rectangle.perimeter(9, 3), 24)


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEquals(square.area(2), 4)
        self.assertEquals(square.area(3), 9)
        self.assertEquals(square.area(4), 16)
        self.assertEquals(square.area(12), 144)
        self.assertEquals(square.area(10), 100)

    def test_perimeter(self):
        self.assertEquals(square.perimeter(0), 0)
        self.assertEquals(square.perimeter(1), 4)
        self.assertEquals(square.perimeter(2), 8)
        self.assertEquals(square.perimeter(3), 12)
        self.assertEquals(square.perimeter(20), 80)


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEquals(triangle.area(1, 4), 2)
        self.assertEquals(triangle.area(4, 4), 8)
        self.assertEquals(triangle.area(3, 5), 7.5)
        self.assertEquals(triangle.area(6, 5), 15)
        self.assertEquals(triangle.area(10, 10), 50)

    def test_perimeter(self):
        self.assertEquals(triangle.perimeter(1, 1, 1), 3)
        self.assertEquals(triangle.perimeter(2, 2, 2), 6)
        self.assertEquals(triangle.perimeter(1, 3, 3), 7)
        self.assertEquals(triangle.perimeter(3, 4, 6), 13)
        self.assertEquals(triangle.perimeter(15, 25, 15), 55)


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEquals(circle.area(1), 1 * math.pi)
        self.assertEquals(circle.area(2), 4 * math.pi)
        self.assertEquals(circle.area(3), 9 * math.pi)
        self.assertEquals(circle.area(4), 16 * math.pi)
        self.assertEquals(circle.area(5), 25 * math.pi)

    def test_perimeter(self):
        self.assertEquals(circle.perimeter(1), 2 * math.pi)
        self.assertEquals(circle.perimeter(2), 4 * math.pi)
        self.assertEquals(circle.perimeter(3), 6 * math.pi)
        self.assertEquals(circle.perimeter(4), 8 * math.pi)
        self.assertEquals(circle.perimeter(5), 10 * math.pi)


if __name__ == '__main__':
    unittest.main()
