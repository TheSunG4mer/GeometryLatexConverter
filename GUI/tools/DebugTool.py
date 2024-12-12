


from GUI.tools.ToolInterface import Tool


class DebugTool(Tool):
    def __init__(self, root):
        self.root = root

    def do_click(self, event, extraButton=None):
        print([str(x) for x in self.root.objects])
        print(f"x values: {self.root.lowerx}, {self.root.upperx}")
        print(f"y values: {self.root.lowery}, {self.root.uppery}")

    def do_drag(self, event, extraButton=None):
        pass

    def do_release(self, event, extraButton=None):
        pass

    def __str__(self):
        return "Debug Tool"
        