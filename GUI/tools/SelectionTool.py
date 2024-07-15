

from GUI.tools.ToolInterface import Tool


class SelectionTool(Tool):
    def __init__(self, root):
        self.root = root

    def do_click(self, event):
        print([str(x) for x in self.root.objects])

    def do_drag(self, event):
        pass

    def do_release(self, event):
        pass
