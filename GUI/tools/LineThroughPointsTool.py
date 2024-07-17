from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from GUI.tools.ToolInterface import Tool
from Objects import Circle
from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.Line import Line
from Objects.Point import Point


class LineThroughPointsTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [2, 0, 0] # Needs 2 points, 0 lines and 0 circles

    
    def __str__(self):
        return "Line Through Two Points Tool"

    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1]]
        line = Line(definingObjects, LineThroughTwoPointsConstruction(), isVisible=True)
        self.root.addObject(line)
        self.root.redraw()