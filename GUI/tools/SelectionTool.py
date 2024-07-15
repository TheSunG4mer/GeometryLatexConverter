

from collections import deque
from GUI.tools.ToolInterface import Tool
from Objects.Point import Point


class SelectionTool(Tool):
    def __init__(self, root):
        self.root = root
        self.selectedObject = None

    def do_click(self, event):
        x, y, = event.x, event.y
        tolerance = self.root.getTolerance()

        for object in self.root.objects:
            if object.isClose(x, y, tolerance):
                selectedObject = object
                break
        else:
            selectedObject = None

        print(selectedObject)       #For debugging 
        self.selectedObject = selectedObject
        self.root.addSelectedObject(selectedObject)

    def do_drag(self, event):
        x, y = event.x, event.y
        if isinstance(self.selectedObject, Point):
            children = self.selectedObject.setCoordinates(x, y)

            objectsToBeUpdated = deque(children)
            while objectsToBeUpdated:
                obj = objectsToBeUpdated.popleft()
                newChildren = obj.correctPosition()
                objectsToBeUpdated.extend(newChildren)
        
        
        self.root.redraw()


    def do_release(self, event):
        pass
        self.root.clearSelectedObjects()
        self.selectedObject = None

    def __str__(self):
        return "Selection Tool"
