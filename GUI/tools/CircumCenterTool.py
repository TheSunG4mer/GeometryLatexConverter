from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.CircumCenterConstruction import CircumCenterConstruction
from Objects.Point import Point


class CircumCenterTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [3,0,0]
    
    def __str__(self):
        return "Circum Center Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1], points[2]]

        point = Point(definingObjects=definingObjects, constructionStrategy=CircumCenterConstruction(), isVisible=True)
        self.root.addObject(point)
        self.root.redraw()

