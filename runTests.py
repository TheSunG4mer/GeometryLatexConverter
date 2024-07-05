import Objects.ConstructionStrategies.LineThroughTwoPointsConstruction as file1
import unittest

from Objects.Point import Point


class TestStringMethods(unittest.TestCase):
    def test_point_gives_right_coordinates(self):
        P = Point(0,1)
        x, y = P.getCoordinates()
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)

    def test_shouldNewPointExist(self):
        P = Point(3,-2)
        self.assertEqual(P.free(), True)

if __name__ == "__main__":
    unittest.main()