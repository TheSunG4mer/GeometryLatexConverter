

from GUI.tools.ToolInterface import Tool


class SelectionTool(Tool):
    def __init__(self, root):
        self.root = root

    def do_click(self, event):
        print("Hello World")

    def do_drag(self, event):
        print("Hello World2")

    def do_release(self, event):
        print("Hello World3")
