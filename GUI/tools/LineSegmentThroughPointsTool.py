from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.LineSegmentThroughTwoPointsConstruction import LineSegmentThroughTwoPointsConstruction
from Objects.Line import Line


class LineSegmentThroughPointsTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [2, 0, 0] # Needs 2 points, 0 lines and 0 circles

    
    def __str__(self):
        return "Line Segment Through Two Points Tool"

    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1]]
        line = Line(definingObjects, LineSegmentThroughTwoPointsConstruction(), isVisible=True)
        self.root.addObject(line)
        self.root.redraw()