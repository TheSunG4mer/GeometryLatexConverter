from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.Line import Line
from Objects.Point import Point


class PointAsProjectionOfPointToLineConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        point, line = definingObjects
        assert isinstance(point, Point)
        assert isinstance(line, Line)

        x, y= point.getCoordinates()
        a, b, c = line.getCoefficients()

        D = a ** 2 + b ** 2
        cPrime = b * x - a * y
        
        x, y = (a * c + b * cPrime) / D, (b * c - a * cPrime) / D
        if line.isPointInBoundingBox((x, y)):
            return x, y
        return None, None
            
