import tkinter

from GUI.tools.PointInsertionTool import PointInsertionTool
from GUI.tools.SelectionTool import SelectionTool
from Objects.Point import Point

RADIUS = 5


class GUI:
    def do_clear(self):
        self.objects.clear()
        self.redraw()

    def do_click(self, event):
        self.currentTool.do_click(event)
        

    def do_drag(self, event):
        pass

    def do_release(self, event):
        pass



    def do_quit(self):
        self.root.destroy()


    def redraw(self):
        self.canvas.delete('all')

        for object in self.objects:
            if isinstance(object, Point):
                x, y = object.getCoordinates()
                self.canvas.create_oval(x-RADIUS, y-RADIUS, x+RADIUS, y+RADIUS, fill='grey')

    def create_menu(self):
        menubar = tkinter.Menu(self.root)
        pointmenu = tkinter.Menu(menubar, tearoff=0)
        pointmenu.add_command(label='Point', command=self.set_current_tool_handler(self.pointInsertionTool))
        colormenu = tkinter.Menu(menubar, tearoff=0)
        for color in self.colors: # list of color names
            colormenu.add_command(label=color,
                                foreground=color)
        menubar.add_cascade(label='Points', menu=pointmenu)
        menubar.add_cascade(label='Color', menu=colormenu)
        self.root.config(menu=menubar) # Show menubar

    def set_current_tool_handler(self, tool):
        return lambda : self.set_current_tool(tool)
    
    def set_current_tool(self, tool):
        print(tool)
        self.currentTool = tool

    def __init__(self, root):
        self.root = root
        self.objects = []
        self.colors = ['black', 'red', 'blue', 'green', 'yellow']

        root.title('Geometry Window')
        root.resizable(True, True)

        # Creating tools for use.
        self.selectionTool = SelectionTool(self)
        self.pointInsertionTool = PointInsertionTool(self)
        
        
        self.currentTool = self.selectionTool


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
        self.canvas = canvas

        self.create_menu()

