


from Objects.Circle import Circle
from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.ConstructionStrategies.PointIntersectionOfLineAndCircleConstruction import PointIntersectionOfLineAndCircleConstruction
from Objects.ConstructionStrategies.RadicalAxisConstruction import RadicalAxisConstruction
from Objects.Line import Line


class PointAsCircleCircleIntersectionConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        circle1, circle2, number = definingObjects
        assert isinstance(circle1, Circle)
        assert isinstance(circle2, Circle)
        assert number in [0, 1]
        
        C1, C2 = circle1.getCenter(), circle2.getCenter()
        x1, y1 = C1.getCoordinates()
        x2, y2 = C2.getCoordinates()
        r1, r2 = circle1.getRadius(), circle2.getRadius()
        d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        D = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
        orthoLength = (r1 ** 2 - D ** 2) ** 0.5


        deltax = (x2 - x1) / d
        deltay = (y2 - y1) / d

        newNumber = 2 * number - 1


        return x1 + D * deltax + newNumber * orthoLength * deltay, \
            y1 + D * deltay - newNumber * orthoLength * deltax
        #PointIntersectionOfLineAndCircleConstruction().constructObject([radicalAxis, circle1, number])