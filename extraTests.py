

from Objects.Circle import Circle
from Objects.ConstructionStrategies.CircleWithCenterAndRadiusConstruction import CircleWithCenterAndRadiusConstruction
from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.ConstructionStrategies.PointIntersectionOfLineAndCircleConstruction import PointIntersectionOfLineAndCircleConstruction
from Objects.Line import Line
from Objects.Point import Point


A = Point(0,0)
B = Point(0,1)
l = Line([A, B], LineThroughTwoPointsConstruction())
c = Circle([A, 2], CircleWithCenterAndRadiusConstruction())
X = Point([l, c, 1], PointIntersectionOfLineAndCircleConstruction())

strat = PointIntersectionOfLineAndCircleConstruction()
print(strat.constructObject([l, c, 0]))
print(strat.findPossibleSolutions(l, c))

print(X.getCoordinates())