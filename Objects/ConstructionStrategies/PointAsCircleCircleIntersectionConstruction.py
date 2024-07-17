


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

        radicalAxis = Line(definingObjects=[circle1, circle2], constructionStrategy=RadicalAxisConstruction())

        return PointIntersectionOfLineAndCircleConstruction().constructObject([radicalAxis, circle1, number])