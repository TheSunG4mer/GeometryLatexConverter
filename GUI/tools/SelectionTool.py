

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
        print(selectedObject)
        self.selectedObject = selectedObject

    def do_drag(self, event):
        x, y = event.x, event.y
        if isinstance(self.selectedObject, Point):
            self.selectedObject.setCoordinates(x, y)
        self.root.redraw()


    def do_release(self, event):
        pass

        self.selectedObject = None

    def __str__(self):
        return "Selection Tool"
