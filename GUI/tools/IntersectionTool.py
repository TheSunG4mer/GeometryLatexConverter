

from GUI.tools.CircleCircleIntersectionTool import CircleCircleIntersectionTool
from GUI.tools.LineCircleIntersectionTool import LineCircleIntersectionTool
from GUI.tools.LineLineIntersectionTool import LineLineIntersectionTool
from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool



class IntersectionTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [0,2,0]
        self.llIntersection = LineLineIntersectionTool(self.root)
        self.lcIntersection = LineCircleIntersectionTool(self.root)
        self.ccIntersection = CircleCircleIntersectionTool(self.root)
    
        
    def hasRightObjects(self, objectTally):
        return objectTally[0] == 0 and objectTally[1] + objectTally[2] == 2

    def hasTooManyObjects(self, objectTally):
        return objectTally[0] > 0 or objectTally[1] + objectTally[2] > 2


    def __str__(self):
        return "Intersection Tool"
    
    def createObject(self):
        objectTally = self.root.getSelectedObjectsTally()
        if objectTally[1] == 2:
            self.llIntersection.createObject()
        elif objectTally[1] == 1:
            self.lcIntersection.createObject()
        elif objectTally[1] == 0:
            self.ccIntersection.createObject()
        