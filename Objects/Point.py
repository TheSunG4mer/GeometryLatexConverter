from Object import GeometricObject

class Point(GeometricObject):

    def __init__(self, x = None, y = None, definingObjects = None, definingRelation = None, name = None):
            
        if not definingObjects:
            self.isFree = True
            self.definingObjects = []
            self.definingRelation = None
            self.x = x
            self.y = y

        else:
            self.isFree = False
            self.definingObjects = definingObjects
            self.definingRelation = definingRelation
            self.x = 0
            self.y = 0
            self.correctPosition()
        
        self.childObjects = []
        self.name = name
    
    def getCoordinates(self):
        return self.x, self.y
    
    def correctPosition(self):
        match self.definingRelation:
            case "intersection":
                pass
            case _:
                pass
        
        return self.childObjects
    