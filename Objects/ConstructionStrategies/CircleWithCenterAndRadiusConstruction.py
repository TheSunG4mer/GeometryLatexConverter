


from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.Point import Point


class CircleWithCenterAndRadiusConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        P, r = definingObjects

        assert isinstance(P, Point)
        assert isinstance(r, int) or isinstance(r, float)

        return P, r
    