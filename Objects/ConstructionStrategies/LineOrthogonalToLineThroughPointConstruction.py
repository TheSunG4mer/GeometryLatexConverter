

from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.Line import Line
from Objects.Point import Point


class LineOrthogonalToLineThroughPointConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        point, line = definingObjects
        assert isinstance(point, Point)
        assert isinstance(line, Line)
        x, y = point.getCoordinates()
        a, b, c = line.getCoefficients()
        
        return b, -a, b * x - a * y, [[None, None], [None, None]]