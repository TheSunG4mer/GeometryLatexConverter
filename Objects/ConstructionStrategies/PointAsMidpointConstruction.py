

from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.Point import Point


class PointAsMidpointConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        point1, point2 = definingObjects
        assert isinstance(point1, Point)
        assert isinstance(point2, Point)
        x1, y1 = point1.getCoordinates()
        x2, y2 = point2.getCoordinates()
        return (x1 + x2)/2, (y1 + y2)/2

        pass