from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.Point import Point


class PointDistanceFromPointAlingLineConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        pointFrom, pointTo, distance = definingObjects
        assert isinstance(pointFrom, Point)
        assert isinstance(pointTo, Point)
        assert isinstance(distance, int) or isinstance(distance, float)
        #assert distance > 0

        x1, y1 = pointFrom.getCoordinates()
        x2, y2 = pointTo.getCoordinates()

        alpha = distance / (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)


        return x1 + alpha * (x2 - x1), y1 + alpha * (y2 - y1)