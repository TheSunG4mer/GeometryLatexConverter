from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.LineOrthogonalToLineThroughPointConstruction import LineOrthogonalToLineThroughPointConstruction
from Objects.ConstructionStrategies.LineParallelToLineThroughPointConstruction import LineParallelToLineThroughPointConstruction
from Objects.Line import Line


class LineParallelThroughPointTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [1,1,0]
    
    def __str__(self):
        return "Orthogonal Line Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], lines[0]]

        line = Line(definingObjects=definingObjects, constructionStrategy=LineParallelToLineThroughPointConstruction(), isVisible=True)
        self.root.addObject(line)
        self.root.redraw()

