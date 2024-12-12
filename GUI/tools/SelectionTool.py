

from collections import deque
from GUI.tools.ToolInterface import Tool
from Objects.Point import Point

def dist2(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)

class SelectionTool(Tool):
    def __init__(self, root):
        self.root = root
        self.selectedObject = None
        self.x, self.y = None, None

    def do_click(self, event, extraButton=None):
        if extraButton is None:
            self.root.clearSelectedObjects()
        x, y, = event.x, event.y
        x, y = self.root.canvas_coords_to_internal_coors(x, y)
        tolerance = self.root.getTolerance()

        # To make sure, that we check point before lines or circles, we check sort them to the front

        geometricObjects = [object for object in self.root.objects if object.exists()]
        geometricObjects.sort(key=lambda obj: isinstance(obj, Point), reverse=True)

        for object in geometricObjects:
            if object.isClose(x, y, tolerance):
                self.selectedObject = object
                self.root.addSelectedObject(object)
                break
        else:
            self.selectedObject = None

        print(self.selectedObject)   #For debugging 
        self.x, self.y = x, y
        
        self.root.redraw()

    def do_drag(self, event, extraButton=None):
        x, y = event.x, event.y
        x, y = self.root.canvas_coords_to_internal_coors(x, y)
        if isinstance(self.selectedObject, Point):
            children = self.selectedObject.setCoordinates(x, y)

            objectsToBeUpdated = deque(children)
            while objectsToBeUpdated:
                obj = objectsToBeUpdated.popleft()
                newChildren = obj.correctPosition()
                objectsToBeUpdated.extend(newChildren)
        
        elif self.selectedObject is None:
            dx, dy = x - self.x, y - self.y
            self.root.moveCanvas(dx, dy)
            self.x, self.y = self.root.canvas_coords_to_internal_coors(event.x, event.y)

        
        self.root.redraw()


    def do_release(self, event, extraButton=None):
        # if not extraButton == "ctrl":
        #     self.root.clearSelectedObjects()
        self.selectedObject = None
        self.x, self.y = None, None
        self.root.redraw()

    def __str__(self):
        return "Selection Tool"
    

