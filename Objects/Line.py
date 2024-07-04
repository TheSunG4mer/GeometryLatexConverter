from Object import GeometricObject

class Line(GeometricObject):
    def __init__(self, definingObjects, definingRelation, name = None, isVisible = False):
        self.definingObjects = definingObjects
        self.definingRelation = definingRelation

        self.xCoef = 1
        self.yCoef = 1
        self.c = 0

        self.correctPosition()

        self.childObjects = []
        self.name = name
        self.isVisible = isVisible

    
    def correctPosition(self):
        match self.definingRelation:
            case "lineThroughPoint":
                pass
            case _:
                pass
        
        return self.childObjects
        