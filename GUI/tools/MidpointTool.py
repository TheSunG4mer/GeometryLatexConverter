from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.PointAsMidpointConstruction import PointAsMidpointConstruction
from Objects.ConstructionStrategies.PointIntersectionOfLineAndCircleConstruction import PointIntersectionOfLineAndCircleConstruction
from Objects.ConstructionStrategies.PointIntersectionOfTwoLines import PointIntersectionOfTwoLinesConstruction
from Objects.Point import Point


class MidpointTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [2,0,0]
    
    def __str__(self):
        return "Midpoint Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1]]

        point = Point(definingObjects=definingObjects, constructionStrategy=PointAsMidpointConstruction(), isVisible=True)
        self.root.addObject(point)
        self.root.redraw()

