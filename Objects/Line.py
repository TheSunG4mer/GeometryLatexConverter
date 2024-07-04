from Object import GeometricObject
from ConstructionStrategies.ConstructionStrategy import ConstructionStrategy


class Line(GeometricObject):
    def __init__(self, definingObjects, constructionStrategy, name = None, isVisible = False):
        
        assert all([isinstance(obj, GeometricObject) for obj in definingObjects])
        assert isinstance(constructionStrategy, ConstructionStrategy)
        self.definingObjects = definingObjects
        self.constructionStrategy = constructionStrategy

        self.xCoef = 1
        self.yCoef = 1
        self.c = 0
        self.doesExist = True

        self.childObjects = []
        self.name = name
        self.isVisible = isVisible

        self.correctPosition()
    
    def correctPosition(self):
        if any([not obj.exists() for obj in self.definingObjects]):
            self.x = None
            self.y = None
            self.doesExist = False
        else:
            self.xCoef, self.yCoef, self.c = self.constructionStrategy.constructObject(self.definingObjects)
            if self.xCoef == None or self.yCoef == None or self.c == None:
                self.doesExist = False
            else:
                self.doesExist = True

        return self.childObjects
        
    def getCoefficients(self):
        return self.xCoef, self.yCoef, self.c

    def exists(self):
        return self.doesExist