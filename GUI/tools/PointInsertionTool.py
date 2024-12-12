from GUI.tools.ToolInterface import Tool
from Objects.Point import Point


class PointInsertionTool(Tool):
    def __init__(self, root):
        self.root = root

    def do_click(self, event, extraButton=None):
        x, y = event.x, event.y
        x, y = self.root.canvas_coords_to_internal_coors(x, y)
        self.root.redraw()
        self.root.drawPoint(x,y, "blue")

    def do_drag(self, event, extraButton=None):
        x, y = event.x, event.y
        x, y = self.root.canvas_coords_to_internal_coors(x, y)
        self.root.redraw()
        self.root.drawPoint(x,y, "blue")
    
    def do_release(self, event, extraButton=None):
        x, y = event.x, event.y
        x, y = self.root.canvas_coords_to_internal_coors(x, y)
        self.root.addObject(Point(x=x, y=y, isVisible=True))
        self.root.redraw()

    def __str__(self):
        return "Point Insertion Tool"
    
