from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.Point import Point


class HalfLineConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        point1, point2 = definingObjects
        assert isinstance(point1, Point)
        assert isinstance(point2, Point)

        a, b, c, boundaries = LineThroughTwoPointsConstruction().constructObject([point1, point2])

        x1, y1 = point1.getCoordinates()
        x2, y2 = point2.getCoordinates()

        if x1 < x2:
            boundaries[0][0] = x1
        else:
            boundaries[1][0] = x1
        
        if y1 < y2:
            boundaries[0][1] = y1
        else:
            boundaries[1][1] = y1

        return a, b, c, boundaries

        return 