from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.ConstructionStrategies.LineOrthogonalToLineThroughPointConstruction import LineOrthogonalToLineThroughPointConstruction
from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.ConstructionStrategies.PointAsMidpointConstruction import PointAsMidpointConstruction
from Objects.Line import Line
from Objects.Point import Point


class PerpendicularBisectorConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        point1, point2 = definingObjects
        assert isinstance(point1, Point)
        assert isinstance(point2, Point)

        l = Line(definingObjects=[point1, point2], constructionStrategy=LineThroughTwoPointsConstruction())
        M = Point(definingObjects=[point1, point2], constructionStrategy=PointAsMidpointConstruction())

        return LineOrthogonalToLineThroughPointConstruction().constructObject([M, l])