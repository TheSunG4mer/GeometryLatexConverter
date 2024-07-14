from scipy.spatial import ConvexHull
import tkinter

RADIUS = 5


class ConvexHullWindow:
    def do_clear(self):
        self.points.clear()
        self.redraw()

    def do_click(self, event):
        x, y = event.x, event.y
        points = self.points
        Q = [p for p in points if (x - p[0])**2 + (y - p[1])**2 <= RADIUS**2]
        if Q:
            points.remove(Q[-1])
        else:
            points.append((x, y))
        self.redraw()

    def redraw(self):
        self.canvas.delete('all')

        if self.show_ch.get() and len(self.points) >= 3:
            convex_hull = [self.points[idx] for idx in ConvexHull(self.points).vertices]
            self.canvas.create_polygon(convex_hull, fill='yellow', outline='black')
        for x, y in self.points:
            self.canvas.create_oval(x-RADIUS, y-RADIUS, x+RADIUS, y+RADIUS, fill='grey')

    def __init__(self, root):
        self.root = root
        self.points = []

        root.title('Convex hull')
        root.resizable(False, False)

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


ConvexHullWindow(tkinter.Tk())
# ConvexHullWindow(tkinter.Toplevel())

tkinter.mainloop()