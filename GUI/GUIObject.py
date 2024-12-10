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


CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600

BUTTON_WIDTH = 5

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
        if not point.free():
            outline = "black"
        else:
            outline = "blue"
        
        if point in self.selectedObjects:
            size = self.largePointSize
        else:
            size = self.smallPointSize

        color = point.getColor() if point.getColor() is not None else "black"

        self.drawPoint(x, y, color=color, size=size, outline=outline)


    def drawPoint(self, x, y, color="grey", outline = "black", size=5):
        x, y = self.internal_coords_to_canvas_coords(x, y)

        # convert to canvas coordinates
        self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline=outline)

    def getBoundingCoordinates(self):
        return [[self.lowerx, self.lowery], [self.upperx, self.uppery]]

    def drawLineObject(self, line):
        assert isinstance(line, Line)
        
        x1, y1, x2, y2 = line.getPlottingCoordinates(self.getBoundingCoordinates())

        # convert to canvas coordinates
        x1, y1 = self.internal_coords_to_canvas_coords(x1, y1)
        x2, y2 = self.internal_coords_to_canvas_coords(x2, y2)

        if line in self.selectedLines:
            width = 3
        else:
            width = 2
        
        color = line.getColor() if line.getColor() is not None else "black"

        self.canvas.create_line(x1, y1, x2, y2, width=width, fill=color)

    def drawCircleObject(self, circle):
        assert isinstance(circle, Circle)
        center = circle.getCenter()
        radius = circle.getRadius()
        x, y = center.getCoordinates()
        if circle in self.selectedCircles:
            width = 3
        else:
            width = 2
        
        # convert to canvas coordinates
        x, y = self.internal_coords_to_canvas_coords(x, y)
        radius = self.internal_distance_to_canvas_distance(radius)

        color = circle.getColor() if circle.getColor() is not None else "black"

        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, width=width, outline=color)

    def canvas_coords_to_internal_coors(self, x, y):
        """
        Convert canvas coordinates to internal coordinates
        """
        alphax = x / CANVAS_WIDTH
        alphay = y / CANVAS_HEIGHT
        return (self.lowerx + alphax * (self.upperx - self.lowerx), self.lowery + alphay * (self.uppery - self.lowery))

    def canvas_distance_to_internal_distance(self, distance):
        """
        Convert canvas distance to internal distance
        """
        return distance * (self.upperx - self.lowerx) / CANVAS_WIDTH

    def internal_coords_to_canvas_coords(self, x, y):
        """
        Convert internal coordinates to canvas coordinates
        """
        alphax = (x - self.lowerx) / (self.upperx - self.lowerx)
        alphay = (y - self.lowery) / (self.uppery - self.lowery)
        return (CANVAS_WIDTH * alphax, CANVAS_HEIGHT * alphay)

    def internal_distance_to_canvas_distance(self, distance):
        """
        Convert internal distance to canvas distance
        """
        return distance * CANVAS_WIDTH / (self.upperx - self.lowerx)

    def moveCanvas(self, dx, dy):
        self.lowerx -= dx
        self.upperx -= dx
        self.lowery -= dy
        self.uppery -= dy
    
    def zoom(self, event):
        if event.delta > 0:
            self.zoom_in(event)
        else:
            self.zoom_out(event)

    def zoom_in(self, event):
        x, y = event.x, event.y
        x, y = self.canvas_coords_to_internal_coors(x, y)
        self.lowerx = x + 0.9 * (self.lowerx - x)
        self.upperx = x + 0.9 * (self.upperx - x)
        self.lowery = y + 0.9 * (self.lowery - y)
        self.uppery = y + 0.9 * (self.uppery - y)
        self.redraw()
    
    def zoom_out(self, event):
        x, y = event.x, event.y
        x, y = self.canvas_coords_to_internal_coors(x, y)
        self.lowerx = x + 1.1 * (self.lowerx - x)
        self.upperx = x + 1.1 * (self.upperx - x)
        self.lowery = y + 1.1 * (self.lowery - y)
        self.uppery = y + 1.1 * (self.uppery - y)
        self.redraw()

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
        movemenu.add_command(label="Reset view", 
                            command=self.reset_view_handler())
        
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
        triangleCenterMenu.add_command(label='Geocenter',
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

    
    def reset_view_handler(self):
        return lambda : self.reset_view()

    def reset_view(self):
        self.lowerx = 0
        self.upperx = CANVAS_WIDTH
        self.lowery = 0
        self.uppery = CANVAS_HEIGHT
        self.redraw()

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

    def setColor(self, color):
        for object in self.selectedObjects:
            object.setColor(color)
        self.redraw()

    def setLabelDirection(self, direction):
        if len(self.selectedObjects) != 1:
            return
        self.selectedObjects[0].setLabelDirection(direction)


    def __init__(self, root):
        self.root = root
        self.objects = []
        self.selectedObjects = []
        self.selectedPoints = []
        self.selectedLines = []
        self.selectedCircles = []
        self.selectedObjectsTally = [0, 0, 0]
        self.colors = ['black', 'red', 'blue', 'green', 'yellow', 'grey', 'purple', 'orange', 'brown', 'pink']


        root.title('Geometry Window')
        root.resizable(False, False)

        self.lowerx = 0
        self.upperx = CANVAS_WIDTH
        self.lowery = 0
        self.uppery = CANVAS_HEIGHT

        self.currentTool = SelectionTool(self)

        self.smallPointSize = SMALLRADIUS
        self.largePointSize = RADIUS
        self.tolerance = TOLERANCE


        button_clear = tkinter.Button(root, text='Clear', command=self.do_clear)
        button_clear.grid(row=0, column=2, sticky='EW')

        self.show_ch = tkinter.IntVar()
        # checkbox = tkinter.Checkbutton(root, text='show convex hull',
        #                                variable=self.show_ch, command=self.redraw)
        # checkbox.grid(row=0, column=2)

        canvas = tkinter.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background='lightgrey')
        canvas.grid(row=1, column=0, rowspan = 30, columnspan=3)
        
        menu_text = tkinter.Label(root, text='Object Menu', width = 5 * BUTTON_WIDTH)
        menu_text.grid(row=0, column=3, columnspan = 5,  sticky='W')


###################################### Color Menu ########################################

        color_text = tkinter.Label(root, text='Choose color', width = 30)
        color_text.grid(row=1, column=3, columnspan = 5,  sticky='W')

        for i, color in enumerate(self.colors):
            button = tkinter.Button(root, background=color, width = BUTTON_WIDTH, command=lambda color=color: self.setColor(color))
            button.grid(row=2 + i // 5, column=3 + (i % 5), sticky='NSEW')

###################################### Label Menu ########################################

        label_text = tkinter.Label(root, text='Label', width = 30)
        label_text.grid(row=4, column=3, columnspan = 5,  sticky='W')

        for i, direction in enumerate(["NW", "N", "NE", "W", "C", "E", "SW", "S", "SE"]):
            if direction == "C":
                label_writer = tkinter.Entry(root, width = BUTTON_WIDTH)
                label_writer.grid(row=6, column=5, sticky='NSEW')
                continue

            button = tkinter.Button(root, text=direction, width = BUTTON_WIDTH, command=lambda direction=direction: self.setLabelDirection(direction))
            button.grid(row=5 + i // 3, column=4 + (i % 3), sticky='NSEW')
        


        canvas.bind('<Button-1>', self.do_click)
        canvas.bind('<B1-Motion>', self.do_drag)
        canvas.bind('<ButtonRelease-1>', self.do_release)
        canvas.bind('<Control-Button-1>', self.do_click_ctrl)
        canvas.bind('<Control-B1-Motion>', self.do_drag_ctrl)
        canvas.bind('<Control-ButtonRelease-1>', self.do_release_ctrl)
        canvas.bind('<MouseWheel>', self.zoom)
        self.canvas = canvas

        self.create_menu()

