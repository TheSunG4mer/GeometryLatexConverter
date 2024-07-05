import unittest

from Objects.Circle import Circle
from Objects.Line import Line
from Objects.Point import Point


from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.ConstructionStrategies.LineSegmentThroughTwoPointsConstruction import LineSegmentThroughTwoPointsConstruction
from Objects.ConstructionStrategies.CircleWithCenterAndRadiusConstruction import CircleWithCenterAndRadiusConstruction




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

    def test_shouldHaveRightBoundaryForLineSegment(self):
        A = Point(0, 5)
        B = Point(2, 1)
        l = Line([A, B], LineSegmentThroughTwoPointsConstruction())
        xCoef, yCoef, c = l.getCoefficients()
        boundaries = l.getBoundaries()

        self.assertEqual(xCoef, 2)
        self.assertEqual(yCoef, 1)
        self.assertEqual(c, 5)
        self.assertEqual(boundaries, [[0, 1], [2, 5]])

    def test_shouldHaveCircleFromCenterAndRadius(self):
        P = Point(2,4)
        r = 3
        c = Circle([P, r], CircleWithCenterAndRadiusConstruction())
        Q = c.getCenter()
        s = c.getRadius()
        self.assertEqual(Q, P)
        self.assertEqual(s, 3)

if __name__ == "__main__":
    unittest.main()