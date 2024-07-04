import sys

sys.path.append("..")

from Point import Point
from Line import Line

from ConstructionStrategies.ConstructionStrategy import ConstructionStrategy

class LineThroughTwoPointsConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        """
        Constructs object from given defining objects.

        >>> A = Point(0,0)
        >>> B = Point(1,1)
        >>> l = Line([A, B], LineThroughTwoPointsConstruction())
        >>> l.getCoefficients()
        (-1.0, 1.0, 0.0)
        
        
        """
        point1, point2 = definingObjects
        
        assert isinstance(point1, Point)
        assert isinstance(point2, Point)
        
        x1, y1 = point1.getCoordinates()
        x2, y2 = point2.getCoordinates()

        deltax, deltay = x2 - x1, y2 - y1

        if not deltax: # vertical line
            return 1, 0, x1
        
        a = -deltay / deltax
        return a, 1., y1 + a * x1

import doctest
doctest.testmod(verbose=True)