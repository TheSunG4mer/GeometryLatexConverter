from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.AngleBisectorConstruction import AngleBisectorConstruction
from Objects.ConstructionStrategies.HalfLineConstruction import HalfLineConstruction
from Objects.ConstructionStrategies.IncenterConstruction import IncenterConstruction
from Objects.Line import Line
from Objects.Point import Point


class IncenterTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [3,0,0]
    
    def __str__(self):
        return "Incenter Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1], points[2]]

        point = Point(definingObjects=definingObjects, constructionStrategy=IncenterConstruction(), isVisible=True)
        self.root.addObject(point)
        self.root.redraw()

