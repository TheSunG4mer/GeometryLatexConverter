from GUI.tools.ToolInterface import Tool
from Objects.Point import Point


class PointInsertionTool(Tool):
    def __init__(self, root):
        self.root = root

    def do_click(self, event):
        x, y = event.x, event.y
        self.root.redraw()
        self.root.drawPoint(x,y, "blue")

    def do_drag(self, event):
        x, y = event.x, event.y
        self.root.redraw()
        self.root.drawPoint(x,y, "blue")
    
    def do_release(self, event):
        x, y = event.x, event.y
        self.root.objects.append(Point(x=x, y=y, isVisible=True))
        self.root.redraw()