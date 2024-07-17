from GUI.tools.ToolInterface import Tool
from Objects import Circle
from Objects.ConstructionStrategies.LineThroughTwoPointsConstruction import LineThroughTwoPointsConstruction
from Objects.Line import Line
from Objects.Point import Point


class LineThroughPointsTool(Tool):
    def __init__(self, root):
        self.root = root
        self.requiredObjects = [2, 0, 0] # Need 2 points, 0 lines and 0 circles

        self.objDict = {Point:0, Line:1, Circle:2}

    def do_click(self, event, extraButton=None):
        x, y, = event.x, event.y
        tolerance = self.root.getTolerance()

        for obj in self.root.objects:
            if obj.isClose(x, y, tolerance):
                ## Try the selected object
                indexForObj = self.objDict[type(obj)]
                currentObjDistribution = self.root.getSelectedObjectsTally().copy()
                print(self.root.getSelectedObjects())
                print(currentObjDistribution)
                currentObjDistribution[indexForObj] += 1

                if self.hasTooManyObjects(currentObjDistribution):
                    pass
                
                selectedObject = obj
                self.root.addSelectedObject(obj)

                if self.hasRightObjects(currentObjDistribution):
                    print(currentObjDistribution)
                    self.createObject()
                    self.root.clearSelectedObjects()
                break
        else:
            selectedObject = None


        print(selectedObject)       #For debugging 


        self.root.redraw()

    def do_drag(self, event, extraButton=None):
        pass

    def do_release(self, event, extraButton=None):
        pass

    def __str__(self):
        return "Line Through Two Points Tool"

    def tryCreatingObject(self):
        if self.hasRightObjects(self.root.getSelectedObjectsTally()):
            self.createObject()
            self.root.clearSelectedObjects()
            return
        elif self.hasTooManyObjects(self.root.getSelectedObjectsTally()):
            self.root.clearSelectedObjects()
    
    def hasRightObjects(self, objectTally):

        combinedObjectCounter = list(zip(objectTally, self.requiredObjects))
        return all([actual == required for actual, required in combinedObjectCounter])
    
    def hasTooManyObjects(self, objectTally):
        combinedObjectCounter = list(zip(objectTally, self.requiredObjects))
        return any([actual > required for actual, required in combinedObjectCounter])

    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1]]
        line = Line(definingObjects, LineThroughTwoPointsConstruction(), isVisible=True)
        self.root.addObject(line)
        self.root.redraw()