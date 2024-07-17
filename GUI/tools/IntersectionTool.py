

from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.PointIntersectionOfTwoLines import PointIntersectionOfTwoLinesConstruction
from Objects.Point import Point


class IntersectionTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [0,2,0]
    
    def __str__(self):
        return "Intersection Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [lines[0], lines[1]]
        point = Point(definingObjects=definingObjects, constructionStrategy= PointIntersectionOfTwoLinesConstruction(), isVisible=True)
        self.root.addObject(point)
        self.root.redraw()