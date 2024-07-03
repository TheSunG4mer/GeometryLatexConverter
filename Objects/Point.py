from Object import GeometricObject

class Point(GeometricObject):

    def __init__(self, x, y, definingObjects = None, definingRelation = None):
        
        assert isinstance(x, float) or isinstance(x, int)
        assert isinstance(y, float) or isinstance(y, int)

        self.x = x
        self.y = y
        
        if not definingObjects:
            self.isFree = True
            self.definingObjects = []
            self.definingRelation = None
        else:
            self.isFree = False
            self.definingObjects = definingObjects
            self.definingRelation = definingRelation
        
        self.childObjects = []
    
    def getCoordinates(self):
        return self.x, self.y
    
    def correctPosition(self):
        match self.definingRelation:
            case "intersection":
                pass
            case _:
                pass
        
        return self.childObjects
    