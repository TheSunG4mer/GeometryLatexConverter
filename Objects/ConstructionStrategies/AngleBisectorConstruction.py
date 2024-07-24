from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.ConstructionStrategies.HalfLineConstruction import HalfLineConstruction
from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.Point import Point


class AngleBisectorConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        point1, point2, point3 = definingObjects
        assert isinstance(point1, Point)
        assert isinstance(point2, Point)
        assert isinstance(point3, Point)

        distance12 = point1.distanceToPoint(point2)
        distance23 = point3.distanceToPoint(point2)

        ratioFromPoint1ToPoint3 = distance12 / (distance12 + distance23)
        x1, y1 = point1.getCoordinates()
        x3, y3 = point3.getCoordinates()
        x, y = x1 + ratioFromPoint1ToPoint3 * (x3 - x1), y1 + ratioFromPoint1ToPoint3 * (y3 - y1)

        pointOnAngleBisector = Point(x, y)
        return HalfLineConstruction().constructObject([point2, pointOnAngleBisector])
