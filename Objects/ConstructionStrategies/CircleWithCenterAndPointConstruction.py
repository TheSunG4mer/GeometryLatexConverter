from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.Point import Point


class CircleWithCenterAndPointConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        P, Q = definingObjects

        assert isinstance(P, Point)
        assert isinstance(Q, Point)

        return P, P.distanceToPoint(Q)
    