from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.AngleBisectorConstruction import AngleBisectorConstruction
from Objects.ConstructionStrategies.HalfLineConstruction import HalfLineConstruction
from Objects.Line import Line


class AngleBisectorTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [3,0,0]
    
    def __str__(self):
        return "Angle Bisector Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1], points[2]]

        line = Line(definingObjects=definingObjects, constructionStrategy=AngleBisectorConstruction(), isVisible=True)
        self.root.addObject(line)
        self.root.redraw()

