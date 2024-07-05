

from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.Line import Line


class PointIntersectionOfTwoLinesConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        line1, line2 = definingObjects
        assert isinstance(line1, Line)
        assert isinstance(line2, Line)

        x1, y1, c1 = line1.getCoefficients()
        x2, y2, c2 = line2.getCoefficients()

        D = x1 * y2 - x2 * y1

        if D == 0: # Lines are parallel or concurrent
            return None, None
        
        x,y = (y2 * c1 - y1 * c2) / D, (x1 * c2 - x2 * c1) / D
        if all([line.isPointInBoundingBox((x, y)) for line in definingObjects]):
            return x, y
        return None, None
            
