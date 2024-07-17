
from Objects.Circle import Circle
from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.ConstructionStrategies.LineOrthogonalToLineThroughPointConstruction import LineOrthogonalToLineThroughPointConstruction
from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.ConstructionStrategies.PointDistanceFromPointAlongLineConstruction import PointDistanceFromPointAlingLineConstruction
from Objects.Line import Line
from Objects.Point import Point


class RadicalAxisConstruction(ConstructionStrategy):
    def constructObject(self, definingObjects):
        circle1, circle2 = definingObjects
        assert isinstance(circle1, Circle)
        assert isinstance(circle2, Circle)
        c1, c2 = circle1.getCenter(), circle2.getCenter()
        r1, r2 = circle1.getRadius(), circle2.getRadius()

        l = Line(definingObjects=[c1, c2], 
                 constructionStrategy=LineThroughTwoPointsConstruction())
        
        d = c1.distanceToPoint(c2)
        distanceToLinePoint = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
        X = Point(definingObjects=[c1, c2, distanceToLinePoint], 
                  constructionStrategy=PointDistanceFromPointAlingLineConstruction())
        radicalAxis = Line(definingObjects=[X, l], 
                           constructionStrategy=LineOrthogonalToLineThroughPointConstruction())
        a, b, c = radicalAxis.getCoefficients()

        return a, b, c, [[None, None], [None, None]]