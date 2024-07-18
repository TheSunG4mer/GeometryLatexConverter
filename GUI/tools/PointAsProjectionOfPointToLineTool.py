from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.LineOrthogonalToLineThroughPointConstruction import LineOrthogonalToLineThroughPointConstruction
from Objects.ConstructionStrategies.LineParallelToLineThroughPointConstruction import LineParallelToLineThroughPointConstruction
from Objects.ConstructionStrategies.PerpendicularBisectorConstruction import PerpendicularBisectorConstruction
from Objects.ConstructionStrategies.PointAsProjectionOfPointToLineConstruction import PointAsProjectionOfPointToLineConstruction
from Objects.Line import Line
from Objects.Point import Point


class PointAsProjectionOfPointToLineTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [1,1,0]
    
    def __str__(self):
        return "Point As Projection Of Point To Line Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], lines[0]]

        point = Point(definingObjects=definingObjects, constructionStrategy=PointAsProjectionOfPointToLineConstruction(), isVisible=True)
        self.root.addObject(point)
        self.root.redraw()

