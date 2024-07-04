from Object import GeometricObject

class Line(GeometricObject):
    def __init__(self, definingObjects, definingRelation, name = None):
        self.definingObjects = definingObjects
        self.definingRelation = definingRelation
        self.name = name

        self.xCoef = 1
        self.yCoef = 1
        self.c = 0

        self.correctPosition()

        self.childObjects = []

    
    def correctPosition(self):
        match self.definingRelation:
            case "lineThroughPoint":
                pass
            case _:
                pass
        
        return self.childObjects
        