from Objects.Point import Point
from Objects.Line import Line

from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy

class LineSegmentThroughTwoPointsConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        """
        Constructs object from given defining objects.        
        """
        point1, point2 = definingObjects
        
        assert isinstance(point1, Point)
        assert isinstance(point2, Point)
        
        x1, y1 = point1.getCoordinates()
        x2, y2 = point2.getCoordinates()

        xmin, xmax = min([x1, x2]), max([x1, x2])
        ymin, ymax = min([y1, y2]), max([y1, y2])

        deltax, deltay = x2 - x1, y2 - y1

        if not deltax: # vertical line
            return 1, 0, x1, [[xmin, ymin], [xmax, ymax]]
        
        a = -deltay / deltax
        return a, 1., y1 + a * x1, [[xmin, ymin], [xmax, ymax]]
