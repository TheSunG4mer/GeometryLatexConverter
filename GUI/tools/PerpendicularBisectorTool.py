from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.LineOrthogonalToLineThroughPointConstruction import LineOrthogonalToLineThroughPointConstruction
from Objects.ConstructionStrategies.LineParallelToLineThroughPointConstruction import LineParallelToLineThroughPointConstruction
from Objects.ConstructionStrategies.PerpendicularBisectorConstruction import PerpendicularBisectorConstruction
from Objects.Line import Line


class PerpendicularBisectorTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [2,0,0]
    
    def __str__(self):
        return "Perpendicular Bisector Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1]]

        line = Line(definingObjects=definingObjects, constructionStrategy=PerpendicularBisectorConstruction(), isVisible=True)
        self.root.addObject(line)
        self.root.redraw()

