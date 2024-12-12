from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.ConstructionStrategies.PerpendicularBisectorConstruction import PerpendicularBisectorConstruction
from Objects.ConstructionStrategies.PointIntersectionOfTwoLines import PointIntersectionOfTwoLinesConstruction
from Objects.Line import Line
from Objects.Point import Point


class CircumCenterConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        point1, point2, point3 = definingObjects
        assert isinstance(point1, Point)
        assert isinstance(point2, Point)
        assert isinstance(point3, Point)

        l1 = Line(definingObjects=[point1, point2], constructionStrategy=PerpendicularBisectorConstruction())
        l2 = Line(definingObjects=[point1, point3], constructionStrategy=PerpendicularBisectorConstruction())

        return PointIntersectionOfTwoLinesConstruction().constructObject([l1, l2])