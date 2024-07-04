from Object import GeometricObject
from Point import Point

class Circle(GeometricObject):

    def __init__(self, definingObjects, definingRelation, name = None, isVisible = False):
        self.definingObjects = definingObjects
        self.definingRelation = definingRelation

        self.center = Point(x = 0, y = 0)
        self.radius = 1

        self.correctPosition()

        self.childObjects = []
        self.name = name
        self.isVisible = isVisible

    
    def correctPosition(self):
        match self.definingRelation:
            case "center-radius":
                pass
            case _:
                pass
        
        return self.childObjects
    