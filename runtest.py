import unittest

from Objects.Circle import Circle
from Objects.ConstructionStrategies.LineOrthogonalToLineThroughPointConstruction import LineOrthogonalToLineThroughPointConstruction
from Objects.ConstructionStrategies.PointAsMidpointConstruction import PointAsMidpointConstruction
from Objects.ConstructionStrategies.PointDistanceFromPointAlongLineConstruction import PointDistanceFromPointAlingLineConstruction
from Objects.Line import Line
from Objects.Point import Point


from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.ConstructionStrategies.LineSegmentThroughTwoPointsConstruction import LineSegmentThroughTwoPointsConstruction
from Objects.ConstructionStrategies.CircleWithCenterAndRadiusConstruction import CircleWithCenterAndRadiusConstruction
from Objects.ConstructionStrategies.PointIntersectionOfTwoLines import PointIntersectionOfTwoLinesConstruction
from Objects.ConstructionStrategies.PointIntersectionOfLineAndCircleConstruction import PointIntersectionOfLineAndCircleConstruction




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

    def test_shouldIntersectionOfLinesBeRight(self):
        A = Point(0,0)
        B = Point(0,2)
        C = Point(2,0)
        D = Point(2,2)
        l1 = Line([A, D], LineThroughTwoPointsConstruction())
        l2 = Line([B, C], LineThroughTwoPointsConstruction())
        X = Point(definingObjects=[l1, l2], constructionStrategy=PointIntersectionOfTwoLinesConstruction())
        self.assertEqual(X.getCoordinates(), (1,1))

    def test_shouldIntersectionOfLinesBeRight2(self):
        A = Point(0,0)
        B = Point(0,5)
        C = Point(2,4)
        D = Point(1,1)
        l1 = Line([A, D], LineThroughTwoPointsConstruction())
        l2 = Line([B, C], LineThroughTwoPointsConstruction())
        X = Point(definingObjects=[l1, l2], constructionStrategy=PointIntersectionOfTwoLinesConstruction())
        self.assertEqual(X.getCoordinates(), (10/3,10/3))

    def test_shouldParallelLinesHaveNoIntersection(self):
        A = Point(0,0)
        B = Point(2,3)
        C = Point(2,4)
        D = Point(0,1)
        l1 = Line([A, D], LineThroughTwoPointsConstruction())
        l2 = Line([B, C], LineThroughTwoPointsConstruction())
        X = Point(definingObjects=[l1, l2], constructionStrategy=PointIntersectionOfTwoLinesConstruction())
        self.assertFalse(X.exists())

    def test_shouldTooShortLineSegmentsNotExistIntersection(self):
        A = Point(0,0)
        B = Point(0,5)
        C = Point(2,4)
        D = Point(1,1)
        l1 = Line([A, D], LineThroughTwoPointsConstruction())
        l2 = Line([B, C], LineSegmentThroughTwoPointsConstruction())
        X = Point(definingObjects=[l1, l2], constructionStrategy=PointIntersectionOfTwoLinesConstruction())
        self.assertFalse(X.exists())

    def test_shouldGiveCorrectIntersectionBetweenLineAndCircle(self):
        A = Point(0,0)
        B = Point(0,1)
        l = Line([A, B], LineThroughTwoPointsConstruction())
        c = Circle([A, 2], CircleWithCenterAndRadiusConstruction())
        X = Point(definingObjects=[l, c, 0], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        Y = Point(definingObjects=[l, c, 1], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        
        self.assertEqual(X.getCoordinates(), (0,2))
        self.assertEqual(Y.getCoordinates(), (0,-2))

    def test_shouldGiveCorrectIntersectionBetweenLineAndCircle2(self):
        A = Point(0,0)
        B = Point(2,0)
        C = Point(2,1)
        l = Line([C, B], LineThroughTwoPointsConstruction())
        c = Circle([A, 2], CircleWithCenterAndRadiusConstruction())
        X = Point(definingObjects=[l, c, 0], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        Y = Point(definingObjects=[l, c, 1], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        
        self.assertEqual(X.getCoordinates(), (2, 0))
        self.assertFalse(Y.exists())

    def test_shouldGiveCorrectIntersectionBetweenLineAndCircle3(self):
        A = Point(0,0)
        B = Point(3,0)
        C = Point(3,1)
        l = Line([C, B], LineThroughTwoPointsConstruction())
        c = Circle([A, 2], CircleWithCenterAndRadiusConstruction())
        X = Point(definingObjects=[l, c, 0], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        Y = Point(definingObjects=[l, c, 1], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        
        self.assertFalse(X.exists())
        self.assertFalse(Y.exists())

    def test_shouldGiveCorrectIntersectionBetweenLineAndCircle4(self):
        A = Point(1,-1)
        B = Point(-1,0)
        C = Point(-2,1)
        l = Line([C, B], LineThroughTwoPointsConstruction())
        c = Circle([A, 1], CircleWithCenterAndRadiusConstruction())
        X = Point(definingObjects=[l, c, 0], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        Y = Point(definingObjects=[l, c, 1], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        
        self.assertEqual(X.getCoordinates(), (1, -2))
        self.assertEqual(Y.getCoordinates(), (0, -1))

    def test_shouldGiveCorrectIntersectionBetweenLineAndCircle5(self):
        A = Point(1,-1)
        B = Point(-1,0)
        C = Point(-2,0)
        l = Line([C, B], LineThroughTwoPointsConstruction())
        c = Circle([A, 1], CircleWithCenterAndRadiusConstruction())
        X = Point(definingObjects=[l, c, 0], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        Y = Point(definingObjects=[l, c, 1], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        
        self.assertEqual(X.getCoordinates(), (1, 0))
        self.assertFalse(Y.exists())

    def test_shouldGiveCorrectIntersectionBetweenLineAndCircle6(self):
        A = Point(1,-1)
        B = Point(-1,0)
        C = Point(-2,-1)
        l = Line([C, B], LineThroughTwoPointsConstruction())
        c = Circle([A, 1], CircleWithCenterAndRadiusConstruction())
        X = Point(definingObjects=[l, c, 0], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        Y = Point(definingObjects=[l, c, 1], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        
        self.assertFalse(X.exists())
        self.assertFalse(Y.exists())
    
    def test_shouldGiveCorrectIntersectionBetweenLineSegmentAndCircle(self):
        A = Point(1,-1)
        B = Point(-1,0)
        C = Point(-2,1)
        l = Line([C, B], LineSegmentThroughTwoPointsConstruction())
        c = Circle([A, 1], CircleWithCenterAndRadiusConstruction())
        X = Point(definingObjects=[l, c, 0], constructionStrategy=PointIntersectionOfLineAndCircleConstruction())
        
        self.assertFalse(X.exists())



    def test_shoulfGiveRightDistance(self):
        A = Point(0,0)
        B = Point(3,4)
        self.assertEqual(A.distanceToPoint(B), 5)

    def test_shouldFindRightMidpoint(self):
        A = Point(2, 1)
        B = Point(1, 3)
        X = Point(definingObjects=[A,B], constructionStrategy=PointAsMidpointConstruction())
        self.assertEqual(X.getCoordinates(), (3/2, 2))
    
    def test_shouldGiveRightPointFromConstruction(self):
        A = Point(2, 1)
        B = Point(2, 5)
        X = Point(definingObjects=[A, B, 2], constructionStrategy=PointDistanceFromPointAlingLineConstruction())
        self.assertEqual(X.getCoordinates(), (2, 3))
    
    def test_shouldGiveRightPointFromConstruction2(self):
        A = Point(2, 1)
        B = Point(6, 5)
        X = Point(definingObjects=[A, B, 2], constructionStrategy=PointDistanceFromPointAlingLineConstruction())
        self.assertEqual(X.getCoordinates(), (2 + 2 ** 0.5, 1 + 2 ** 0.5))
    
    def test_shouldGiveRightOrthogonalLine(self):
        A = Point(0, 0)
        B = Point(1, 0)
        l1 = Line(definingObjects=[A, B], constructionStrategy=LineThroughTwoPointsConstruction())
        l2 = Line(definingObjects=[A, l1], constructionStrategy=LineOrthogonalToLineThroughPointConstruction())
        
        self.assertEqual(l2.getCoefficients(), (1, 0, 0))

    def test_shouldGiveRightDigagonalLineFromOrthogonalLine(self):
        A = Point(0, 0)
        B = Point(1, 1)
        l1 = Line(definingObjects=[A, B], constructionStrategy=LineThroughTwoPointsConstruction())
        l2 = Line(definingObjects=[B, l1], constructionStrategy=LineOrthogonalToLineThroughPointConstruction())
        
        self.assertEqual(l2.getCoefficients(), (1, 1, 2))


if __name__ == "__main__":
    unittest.main()