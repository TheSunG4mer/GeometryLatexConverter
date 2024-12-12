from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.PointIntersectionOfLineAndCircleConstruction import PointIntersectionOfLineAndCircleConstruction
from Objects.ConstructionStrategies.PointIntersectionOfTwoLines import PointIntersectionOfTwoLinesConstruction
from Objects.Point import Point


class LineCircleIntersectionTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [0,1,1]
    
    def __str__(self):
        return "Line-Circle Intersection Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects1 = [lines[0], circles[0], 0]
        definingObjects2 = [lines[0], circles[0], 1]

        point1 = Point(definingObjects=definingObjects1, constructionStrategy=PointIntersectionOfLineAndCircleConstruction(), isVisible=True)
        point2 = Point(definingObjects=definingObjects2, constructionStrategy=PointIntersectionOfLineAndCircleConstruction(), isVisible=True)
        self.root.addObject(point1)
        self.root.addObject(point2)
        self.root.redraw()