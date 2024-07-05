from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.Object import GeometricObject

class Point(GeometricObject):

    def __init__(self, x = None, y = None, definingObjects = None, 
                constructionStrategy = None, name = None, isVisible = False):
        
        self.childObjects = []
        self.name = name
        self.isVisible = isVisible
        
        
        if not definingObjects:
            self.isFree = True
            self.definingObjects = []
            self.constructionStrategy = None
            self.x = x
            self.y = y
            self.doesExist = True

        else:
            assert isinstance(constructionStrategy, ConstructionStrategy)
            self.isFree = False
            self.definingObjects = definingObjects
            self.constructionStrategy = constructionStrategy
            self.x = 0
            self.y = 0
            self.doesExist = True
            self.correctPosition()
        

    def correctPosition(self):
        if any([not obj.exists() for obj in self.definingObjects if isinstance(obj, GeometricObject)]):
            self.x = None
            self.y = None
            self.doesExist = False
        else:
            if not self.isFree:
                self.x, self.y = self.constructionStrategy.constructObject(self.definingObjects)
            if self.x == None or self.y == None:
                self.doesExist = False
            else:
                self.doesExist = True

        return self.childObjects
    
        
    def getCoordinates(self):
        return self.x, self.y
    
    def exists(self):
        return self.doesExist

    def free(self):
        return self.isFree