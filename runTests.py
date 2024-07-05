import unittest

from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.Line import Line
from Objects.Point import Point


class TestStringMethods(unittest.TestCase):
    def test_point_gives_right_coordinates(self):
        P = Point(0,1)
        x, y = P.getCoordinates()
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)

    def test_shouldNewPointFree(self):
        P = Point(3,-2)
        self.assertEqual(P.free(), True)

    def test_shouldNewPointExist(self):
        P = Point(1,2)
        self.assertEqual(P.exists(), True)
        
    def test_shouldCreateCorrectLine(self):
        A = Point(0,0)
        B = Point(1,1)
        l = Line([A, B], LineThroughTwoPointsConstruction())
        xCoef, yCoef, c = l.getCoefficients()
        boundaries = l.getBoundaries()

        self.assertEqual(xCoef, -1)
        self.assertEqual(yCoef, 1)
        self.assertEqual(c, 0)
        self.assertEqual(boundaries, [[None, None], [None, None]])

    def test_shouldCreateVerticalLine(self):
        A = Point(-11,2)
        B = Point(-11,4)
        l = Line([A, B], LineThroughTwoPointsConstruction())
        xCoef, yCoef, c = l.getCoefficients()
        boundaries = l.getBoundaries()

        self.assertEqual(xCoef, 1)
        self.assertEqual(yCoef, 0)
        self.assertEqual(c, -11)
        self.assertEqual(boundaries, [[None, None], [None, None]])



if __name__ == "__main__":
    unittest.main()