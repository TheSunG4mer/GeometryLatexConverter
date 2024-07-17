import tkinter

from GUI.tools.CircleCircleIntersectionTool import CircleCircleIntersectionTool
from GUI.tools.CircleFromCenterAndPointTool import CircleFromCenterAndPointTool
from GUI.tools.DebugTool import DebugTool
from GUI.tools.IntersectionTool import IntersectionTool
from GUI.tools.LineCircleIntersectionTool import LineCircleIntersectionTool
from GUI.tools.LineThroughPointsTool import LineThroughPointsTool
from GUI.tools.PointInsertionTool import PointInsertionTool
from GUI.tools.SelectionTool import SelectionTool
from Objects.Circle import Circle
from Objects.Line import Line
from Objects.Object import GeometricObject
from Objects.Point import Point

SMALLRADIUS = 4
RADIUS = 5
LARGERADIUS = 7
TOLERANCE = 10


class GUI:
    def do_clear(self):
        self.objects.clear()
        self.redraw()

    def do_click(self, event):
        self.currentTool.do_click(event)
        

    def do_drag(self, event):
        self.currentTool.do_drag(event)

    def do_release(self, event):
        self.currentTool.do_release(event)
        
    
    def do_click_ctrl(self, event):
        self.currentTool.do_click(event, extraButton = "ctrl")
        

    def do_drag_ctrl(self, event):
        self.currentTool.do_drag(event, extraButton = "ctrl")

    def do_release_ctrl(self, event):
        self.currentTool.do_release(event, extraButton = "ctrl")



    def do_quit(self):
        self.root.destroy()

    def drawPointObject(self, point):
        x, y = point.getCoordinates()
        color = "grey"
        if not point.free():
            size = self.smallPointSize
        else:
            size = self.largePointSize
        
        if point in self.selectedObjects:
            color = "blue"
        
        self.drawPoint(x, y, color=color, size=size)


    def drawPoint(self, x, y, color="grey", size=5):
        self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)

    def drawLineObject(self, line):
        assert isinstance(line, Line)
        a, b, c = line.getCoefficients()
        lowerx = self.lowerx
        upperx = self.upperx
        lowery = self.lowery
        uppery = self.uppery

        if b == 0:
            x1 = c / a
            if not lowerx <= x1 <= upperx:
                return
            y1 = lowery
            y2 = uppery
            x2 = x1
        elif a == 0:
            y1= c / b
            if not lowery <= y1 <= uppery:
                return
            x1 = lowerx
            x2 = upperx
            y2 = y1 
        else:
            points = []
            x = (c - b * lowery) / a
            if lowerx <= x <= upperx:
                points.append(x)
                points.append(lowery)
            x = (c - b * uppery) / a
            if lowerx <= x <= upperx:
                points.append(x)
                points.append(uppery)
            y = (c - a * lowerx) / b
            if lowery <= y <= uppery:
                points.append(lowerx)
                points.append(y)
            y = (c - a * upperx) / b
            if lowery <= y <= uppery:
                points.append(upperx)
                points.append(y)
            x1, y1, x2, y2 = points

        if line in self.selectedLines:
            width = 3
        else:
            width = 2
            
        self.canvas.create_line(x1, y1, x2, y2, width=width)

    def drawCircleObject(self, circle):
        assert isinstance(circle, Circle)
        center = circle.getCenter()
        radius = circle.getRadius()
        x, y = center.getCoordinates()
        if circle in self.selectedCircles:
            width = 3
        else:
            width = 2
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, width=width)



    def redraw(self):
        self.canvas.delete('all')
        

        for boolVar in [False, True]:
            for objType in [Circle, Line, Point]:
                for obj in self.objects:
                    if isinstance(obj, objType) and obj.getVisibility() and obj.exists():

                        if isinstance(obj, Point) and obj.free() == boolVar:
                            self.drawPointObject(obj)

                        if isinstance(obj, Line) and not boolVar:
                            self.drawLineObject(obj)

                        if isinstance(obj, Circle) and not boolVar:
                            self.drawCircleObject(obj)


    def create_menu(self):
        menubar = tkinter.Menu(self.root)

        movemenu = tkinter.Menu(menubar, tearoff=0)
        movemenu.add_command(label="Move", 
                             command=self.set_current_tool_handler(self.selectionTool))
        movemenu.add_command(label="Debug Tool", 
                             command=self.set_current_tool_handler(self.debugTool))
        
        pointmenu = tkinter.Menu(menubar, tearoff=0)
        pointmenu.add_command(label='Point', 
                              command=self.set_current_tool_handler(self.pointInsertionTool))
        pointmenu.add_command(label='Intersection', 
                              command=self.set_current_tool_handler(self.intersectionTool))
        pointmenu.add_command(label='LineCircleIntersection', 
                              command=self.set_current_tool_handler(self.lineCircleIntersectionTool))
        pointmenu.add_command(label='CircleCircleIntersection', 
                              command=self.set_current_tool_handler(self.circleCircleIntersectionTool))
        

        linemenu = tkinter.Menu(menubar, tearoff=0)
        linemenu.add_command(label='Line Through Two Points', 
                             command=self.set_current_tool_handler(self.lineThroughTwoPointsTool))

        circlemenu = tkinter.Menu(menubar, tearoff=0)
        circlemenu.add_command(label='Circle from Center and Point', 
                               command=self.set_current_tool_handler(self.circleFromCenterAndPointTool))

        colormenu = tkinter.Menu(menubar, tearoff=0)
        for color in self.colors: # list of color names
            colormenu.add_command(label=color,
                                foreground=color)
        menubar.add_cascade(label='Move', menu=movemenu)
        menubar.add_cascade(label='Points', menu=pointmenu)
        menubar.add_cascade(label='Lines', menu=linemenu)
        menubar.add_cascade(label='Circles', menu=circlemenu)
        menubar.add_cascade(label='Color', menu=colormenu)
        self.root.config(menu=menubar) # Show menubar

    def set_current_tool_handler(self, tool):
        return lambda : self.set_current_tool(tool)
    
    def set_current_tool(self, tool):
        print(f"Active tool: {tool}")
        self.currentTool = tool
        tool.tryCreatingObject()

    def getTolerance(self):
        return self.tolerance
    
    def addObject(self, object):
        self.objects.append(object)

    def addSelectedObject(self, object):
        self.selectedObjects.append(object)
        if isinstance(object, Point):
            self.selectedPoints.append(object)
            self.selectedObjectsTally[0] += 1
        elif isinstance(object, Line):
            self.selectedLines.append(object)
            self.selectedObjectsTally[1] += 1
        elif isinstance(object, Circle):
            self.selectedCircles.append(object)
            self.selectedObjectsTally[2] += 1

    def clearSelectedObjects(self):
        self.selectedObjects = []
        self.selectedPoints = []
        self.selectedLines = []
        self.selectedCircles = []
        self.selectedObjectsTally = [0, 0, 0]

    def getSelectedObjects(self):
        return self.selectedObjects
    
    def getSelectedSortedObjects(self):
        return [self.selectedPoints, self.selectedLines, self.selectedCircles]

    def getSelectedObjectsTally(self):
        return self.selectedObjectsTally

    def __init__(self, root):
        self.root = root
        self.objects = []
        self.selectedObjects = []
        self.selectedPoints = []
        self.selectedLines = []
        self.selectedCircles = []
        self.selectedObjectsTally = [0, 0, 0]
        self.colors = ['black', 'red', 'blue', 'green', 'yellow']


        root.title('Geometry Window')
        root.resizable(False, False)

        self.lowerx = 0
        self.upperx = 1000
        self.lowery = 0
        self.uppery = 600

        # Creating tools for use.
        self.selectionTool = SelectionTool(self)
        self.debugTool = DebugTool(self)

        self.pointInsertionTool = PointInsertionTool(self)
        self.intersectionTool = IntersectionTool(self)
        self.lineCircleIntersectionTool = LineCircleIntersectionTool(self)
        self.circleCircleIntersectionTool = CircleCircleIntersectionTool(self)
        
        self.lineThroughTwoPointsTool = LineThroughPointsTool(self)

        self.circleFromCenterAndPointTool = CircleFromCenterAndPointTool(self)
        
        
        self.currentTool = self.selectionTool

        self.smallPointSize = SMALLRADIUS
        self.largePointSize = RADIUS
        self.veryLargePointSize = LARGERADIUS
        self.tolerance = TOLERANCE


        button_clear = tkinter.Button(root, text='Clear', command=self.do_clear)
        button_clear.grid(row=0, column=1, sticky='EW')

        self.show_ch = tkinter.IntVar()
        checkbox = tkinter.Checkbutton(root, text='show convex hull',
                                       variable=self.show_ch, command=self.redraw)
        checkbox.grid(row=0, column=2)

        canvas = tkinter.Canvas(root, width=1000, height=600, background='lightgrey')
        canvas.grid(row=1, column=0, columnspan=3)
        canvas.bind('<Button-1>', self.do_click)
        canvas.bind('<B1-Motion>', self.do_drag)
        canvas.bind('<ButtonRelease-1>', self.do_release)
        canvas.bind('<Control-Button-1>', self.do_click_ctrl)
        canvas.bind('<Control-B1-Motion>', self.do_drag_ctrl)
        canvas.bind('<Control-ButtonRelease-1>', self.do_release_ctrl)
        self.canvas = canvas

        self.create_menu()

