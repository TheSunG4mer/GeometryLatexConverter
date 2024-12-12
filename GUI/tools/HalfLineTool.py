from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.CircleThroughThreePointsConstruction import CircleThroughThreePointsConstruction
from Objects.ConstructionStrategies.HalfLineConstruction import HalfLineConstruction
from Objects.Line import Line


class HalfLineTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [2,0,0]
    
    def __str__(self):
        return "Half Line Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1]]

        line = Line(definingObjects=definingObjects, constructionStrategy=HalfLineConstruction(), isVisible=True)
        self.root.addObject(line)
        self.root.redraw()

