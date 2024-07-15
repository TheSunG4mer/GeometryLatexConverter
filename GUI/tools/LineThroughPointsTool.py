

from GUI.tools.ToolInterface import Tool
from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.Line import Line


class LineThroughPointsTool(Tool):
    def __init__(self, root):
        self.root = root
        self.requiredObjects = [2, 0, 0] # Need 2 points, 0 lines and 0 circles

    def do_click(self, event, extraButton=None):
        pass

    def do_drag(self, event, extraButton=None):
        pass

    def do_release(self, event, extraButton=None):
        pass

    def __str__(self):
        return "Line Through Two Points Tool"

    def tryCreatingObject(self):
        

        if self.hasRightObjects():
            self.createObject()
            return
        elif self.hasTooManyObjects():
            self.root.clearSelectedObjects()
    
    def hasRightObjects(self):
        combinedObjectCounter = list(zip(self.root.getSelectedObjectsTally(), self.requiredObjects))
        return all([actual == required for actual, required in combinedObjectCounter])
    
    def hasTooManyObjects(self):
        combinedObjectCounter = list(zip(self.root.getSelectedObjectsTally(), self.requiredObjects))
        return any([actual > required for actual, required in combinedObjectCounter])

    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1]]
        line = Line(definingObjects, LineThroughTwoPointsConstruction(), isVisible=True)
        self.root.addObject(line)
        self.root.redraw()