from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.ConstructionStrategies.HalfLineConstruction import HalfLineConstruction
from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.Point import Point


class IncenterConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        point1, point2, point3 = definingObjects
        assert isinstance(point1, Point)
        assert isinstance(point2, Point)
        assert isinstance(point3, Point)

        a = point3.distanceToPoint(point2)
        b = point3.distanceToPoint(point1)
        c = point1.distanceToPoint(point2)

        x1, y1 = point1.getCoordinates()
        x2, y2 = point2.getCoordinates()
        x3, y3 = point3.getCoordinates()

        return (a * x1 + b * x2 + c * x3)/(a + b + c), (a * y1 + b * y2 + c * y3)/(a + b + c)
