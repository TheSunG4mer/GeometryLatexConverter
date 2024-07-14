import tkinter

from GUI.tools import SelectionTool
from Objects.Point import Point

RADIUS = 5


class GUI:
    

    def do_clear(self):
        self.objects.clear()
        self.redraw()

    def do_click(self, event):
        x, y = event.x, event.y
        self.objects.append(Point(x=x, y=y))
        self.redraw()

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
        self.current_tool = tool

    def __init__(self, root):
        self.root = root
        self.objects = []
        self.colors = ['black', 'red', 'blue', 'green', 'yellow']
        self.create_menu()

        root.title('Geometry Window')
        root.resizable(True, True)

        # Creating tools for use.
        self.selectionTool = SelectionTool(self)
        self.current_tool = self.selectionTool

        button_quit = tkinter.Button(root, text='Quit', command=self.root.destroy)
        button_quit.grid(row=0, column=0, sticky='EW')

        button_clear = tkinter.Button(root, text='Clear', command=self.do_clear)
        button_clear.grid(row=0, column=1, sticky='EW')

        self.show_ch = tkinter.IntVar()
        checkbox = tkinter.Checkbutton(root, text='show convex hull',
                                       variable=self.show_ch, command=self.redraw)
        checkbox.grid(row=0, column=2)

        canvas = tkinter.Canvas(root, width=500, height=300, background='lightgrey')
        canvas.grid(row=1, column=0, columnspan=3)
        canvas.bind('<Button-1>', self.do_click)
        self.canvas = canvas


