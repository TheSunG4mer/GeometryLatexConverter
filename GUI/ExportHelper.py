

import datetime

from GUI.GUIObject import GUI
from Objects.Circle import Circle
from Objects.Line import Line
from Objects.Object import GeometricObject
from Objects.Point import Point




def convert_picture_to_tikz(root):
    """
    Convert the picture to a TikZ file.

    :param objects: The objects to convert.
    :param canvas_boundary: The boundary of the canvas.
    """
    assert isinstance(root, GUI)

    objects = root.getObjects()

    now = datetime.datetime.now()
    time_string = now.strftime("%d-%m-%Y--%H-%M-%S")
    print(time_string)
    print(type(time_string))
    filename = "tikzFiles\\tikzPicture" + time_string + ".tex"

    with open(filename, "w") as file:
        file.write("\\begin{tikzpicture}\n")
        for obj in objects:
            file.write(get_code_for_object(obj, root) + "\n")
        file.write("\\end{tikzpicture}\n")


def get_code_for_object(obj, root):
    """
    Get the TikZ code for an object.

    :param obj: The object to get the code for.
    :return: The TikZ code for the object.
    """
    if isinstance(obj, Point):
        return point_to_tikz(obj, root)
    elif isinstance(obj, Line):
        return line_to_tikz(obj, root)
    elif isinstance(obj, Circle):
        return circle_to_tikz(obj, root)


def point_to_tikz(point, root):
    """
    Convert a point to TikZ code.

    :param point: The point to convert.
    :return: The TikZ code for the point.
    """
    assert isinstance(point, Point)
    assert isinstance(root, GUI)
    x, y = point.getCoordinates()
    x, y = root.internal_coords_to_canvas_coords(x, y)

    visible_marker = get_visible_marker(point)
    label_marker = get_label_marker(point, root)
    if point.getVisibility() or point.getLabelVisibility():
        return "\\node[{2},{3}] at ({0},{1}) {};".format(x / 100, y / 100, visible_marker, label_marker)


def line_to_tikz(line):
    """
    Convert a line to TikZ code.

    :param line: The line to convert.
    :return: The TikZ code for the line.
    """
    return "\\draw ({0},{1}) -- ({2},{3});".format(line.p1.x, line.p1.y, line.p2.x, line.p2.y)

def circle_to_tikz(circle):
    """
    Convert a circle to TikZ code.

    :param circle: The circle to convert.
    :return: The TikZ code for the circle.
    """
    return "\\draw ({0},{1}) circle ({2});".format(circle.center.x, circle.center.y, circle.radius)

def get_visible_marker(obj):
    assert isinstance(obj, GeometricObject)
    if obj.getVisibility():
        return "draw, fill = {0}, circle, inner sep = 0, minimum size = 4pt".format(obj.getColor())
    else:
        return ""

def get_label_marker(obj):
    assert isinstance(obj, GeometricObject)
    if obj.getLabelVisibility():
        direction = obj.getLabelDirection()
        direction = convert_direction_to_full_direction(direction)
        return "label={[centered, label distance = {1}]{2}:{{${0}$}}".format(obj.getLabel(), obj.getLabelDistance() / 100, direction)
    else:
        return ""

def convert_direction_to_full_direction(direction):
    if direction == "N":
        return "north"
    elif direction == "S":
        return "south"
    elif direction == "E":
        return "east"
    elif direction == "W":
        return "west"
    elif direction == "NE":
        return "north east"
    elif direction == "NW":
        return "north west"
    elif direction == "SE":
        return "south east"
    elif direction == "SW":
        return "south west"
    else:
        return ""
