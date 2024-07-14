
from Objects.Line import Line
from Objects.Circle import Circle
from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy


class PointIntersectionOfLineAndCircleConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        line, circle, number = definingObjects
        assert isinstance(line, Line)
        assert number in [0,1]
        L = self.findPossibleSolutions(line, circle)
        if len(L) < number + 1:
            return None, None
        x, y =  L[number]
        if line.isPointInBoundingBox((x, y)):
            return x, y
        return None, None
        

    
    def findPossibleSolutions(self, line, circle):
        assert isinstance(line, Line)
        assert isinstance(circle, Circle)
        a, b, c = line.getCoefficients()
        P = circle.getCenter()
        r = circle.getRadius()

        x0, y0 = P.getCoordinates()

        if b == 0:
            x = c / a
            D = r ** 2 - (x - x0) ** 2

            if D < 0:
                return []
            
            elif D == 0:
                return [(x, y0)]
            
            sqD = D ** 0.5
            Y = [y0 + sqD, y0 - sqD]
            return [(x, y) for y in Y]
        
        # now b!=0, i.e. line is not vertical!
        A = 1 + (a / b) ** 2
        B = -2 * (x0 + a * c / (b ** 2) - y0 * a / b)
        C = x0 ** 2 + (c / b) ** 2 - 2 * y0 * c / b + y0 ** 2 - r ** 2
        D = B ** 2 - 4 * A * C
        if D < 0:
            return []
        
        elif D == 0:
            x = - B / (2 * A)
            return [(x, (c - a * x)/ b)]
        sqD = D ** 0.5
        X = [(-B + sqD) / (2 * A), (-B - sqD) / (2 * A)]
        return [(x, (c - a * x) / b) for x in X]