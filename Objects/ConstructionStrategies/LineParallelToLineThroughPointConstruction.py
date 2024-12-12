

from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.Line import Line
from Objects.Point import Point


class LineParallelToLineThroughPointConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        point, line = definingObjects
        assert isinstance(point, Point)
        assert isinstance(line, Line)
        x, y = point.getCoordinates()
        a, b, c = line.getCoefficients()
        
        return a, b, a * x + b * y, [[None, None], [None, None]]