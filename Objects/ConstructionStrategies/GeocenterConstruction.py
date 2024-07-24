from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.ConstructionStrategies.PerpendicularBisectorConstruction import PerpendicularBisectorConstruction
from Objects.ConstructionStrategies.PointIntersectionOfTwoLines import PointIntersectionOfTwoLinesConstruction
from Objects.Line import Line
from Objects.Point import Point


class GeocenterConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        point1, point2, point3 = definingObjects
        assert isinstance(point1, Point)
        assert isinstance(point2, Point)
        assert isinstance(point3, Point)

        x1, y1 = point1.getCoordinates()
        x2, y2 = point2.getCoordinates()
        x3, y3 = point3.getCoordinates()

        return (x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3