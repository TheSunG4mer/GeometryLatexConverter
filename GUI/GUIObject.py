import tkinter

from GUI.tools.AngleBisectorTool import AngleBisectorTool
from GUI.tools.CircleCircleIntersectionTool import CircleCircleIntersectionTool
from GUI.tools.CircleFromCenterAndPointTool import CircleFromCenterAndPointTool
from GUI.tools.CircleThroughThreePointsTool import CircleThroughThreePointsTool
from GUI.tools.CircumCenterTool import CircumCenterTool
from GUI.tools.DebugTool import DebugTool
from GUI.tools.GeocenterTool import GeocenterTool
from GUI.tools.HalfLineTool import HalfLineTool
from GUI.tools.IncenterTool import IncenterTool
from GUI.tools.IntersectionTool import IntersectionTool
from GUI.tools.LineCircleIntersectionTool import LineCircleIntersectionTool
from GUI.tools.LineOrthogonalThroughPointTool import LineOrthogonalThroughPointTool
from GUI.tools.LineParallelThroughPointTool import LineParallelThroughPointTool
from GUI.tools.LineSegmentThroughPointsTool import LineSegmentThroughPointsTool
from GUI.tools.LineThroughPointsTool import LineThroughPointsTool
from GUI.tools.MidpointTool import MidpointTool
from GUI.tools.PerpendicularBisectorTool import PerpendicularBisectorTool
from GUI.tools.PointAsProjectionOfPointToLineTool import PointAsProjectionOfPointToLineTool
from GUI.tools.PointInsertionTool import PointInsertionTool
from GUI.tools.SelectionTool import SelectionTool
from Objects.Circle import Circle
from Objects.Line import Line
from Objects.Object import GeometricObject
from Objects.Point import Point

SMALLRADIUS = 4
RADIUS = 5
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

    def getBoundingCoordinates(self):
        return [[self.lowerx, self.lowery], [self.upperx, self.uppery]]

    def drawLineObject(self, line):
        assert isinstance(line, Line)
        
        x1, y1, x2, y2 = line.getPlottingCoordinates(self.getBoundingCoordinates())

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
                             command=self.set_current_tool_handler(SelectionTool(self)))
        movemenu.add_command(label="Debug Tool", 
                             command=self.set_current_tool_handler(DebugTool(self)))
        
        pointmenu = tkinter.Menu(menubar, tearoff=0)
        pointmenu.add_command(label='Point', 
                              command=self.set_current_tool_handler(PointInsertionTool(self)))
        pointmenu.add_command(label='Intersection', 
                              command=self.set_current_tool_handler(IntersectionTool(self)))
        pointmenu.add_command(label='Midpoint', 
                              command=self.set_current_tool_handler(MidpointTool(self)))
        pointmenu.add_command(label='Projection of Point to Line', 
                              command=self.set_current_tool_handler(PointAsProjectionOfPointToLineTool(self)))

        linemenu = tkinter.Menu(menubar, tearoff=0)
        linemenu.add_command(label='Line Through Two Points', 
                             command=self.set_current_tool_handler(LineThroughPointsTool(self)))
        linemenu.add_command(label='Linesegment Through Two Points', 
                             command=self.set_current_tool_handler(LineSegmentThroughPointsTool(self)))
        linemenu.add_command(label='Halfline Through Two Points', 
                             command=self.set_current_tool_handler(HalfLineTool(self)))
        linemenu.add_command(label='Parallel Line Through Point', 
                             command=self.set_current_tool_handler(LineParallelThroughPointTool(self)))
        linemenu.add_command(label='Orthogonal Line Through Point', 
                             command=self.set_current_tool_handler(LineOrthogonalThroughPointTool(self)))
        linemenu.add_command(label='Perpendicular Bisector', 
                             command=self.set_current_tool_handler(PerpendicularBisectorTool(self)))
        linemenu.add_command(label='Angle Bisector', 
                             command=self.set_current_tool_handler(AngleBisectorTool(self)))
        
        

        circlemenu = tkinter.Menu(menubar, tearoff=0)
        circlemenu.add_command(label='Circle from Center and Point', 
                               command=self.set_current_tool_handler(CircleFromCenterAndPointTool(self)))
        circlemenu.add_command(label='Circle Through Three Points', 
                               command=self.set_current_tool_handler(CircleThroughThreePointsTool(self)))

        triangleCenterMenu = tkinter.Menu(menubar, tearoff=0)
        triangleCenterMenu.add_command(label='Circumcenter',
                                command=self.set_current_tool_handler(CircumCenterTool(self)))
        triangleCenterMenu.add_command(label='Geocumcenter',
                                command=self.set_current_tool_handler(GeocenterTool(self)))
        triangleCenterMenu.add_command(label='Incenter',
                                command=self.set_current_tool_handler(IncenterTool(self)))

        colormenu = tkinter.Menu(menubar, tearoff=0)
        for color in self.colors: # list of color names
            colormenu.add_command(label=color,
                                foreground=color)
        menubar.add_cascade(label='Move', menu=movemenu)
        menubar.add_cascade(label='Points', menu=pointmenu)
        menubar.add_cascade(label='Lines', menu=linemenu)
        menubar.add_cascade(label='Circles', menu=circlemenu)
        menubar.add_cascade(label='Triangle Centers', menu=triangleCenterMenu)
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

        self.currentTool = SelectionTool(self)

        self.smallPointSize = SMALLRADIUS
        self.largePointSize = RADIUS
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

