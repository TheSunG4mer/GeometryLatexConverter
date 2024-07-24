from Objects.ConstructionStrategies.CircleWithCenterAndPointConstruction import CircleWithCenterAndPointConstruction
from Objects.ConstructionStrategies.CircumCenterConstruction import CircumCenterConstruction
from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.Point import Point


class CircleThroughThreePointsConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        point1, point2, point3 = definingObjects
        assert isinstance(point1, Point)
        assert isinstance(point2, Point)
        assert isinstance(point3, Point)

        circumCenter = Point(definingObjects=[point1, point2, point3], 
                             constructionStrategy=CircumCenterConstruction())

        return CircleWithCenterAndPointConstruction().constructObject([circumCenter, point1])