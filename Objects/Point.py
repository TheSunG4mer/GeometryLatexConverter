from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy
from Objects.Object import GeometricObject

class Point(GeometricObject):

    def __init__(self, x = None, y = None, definingObjects = None, 
                constructionStrategy = None, name = None, isVisible = False):

        self.childObjects = []
        self.name = name
        self.isVisible = isVisible
        
        
        if not definingObjects:
            assert isinstance(x, int) or isinstance(x, float)
            assert isinstance(y, int) or isinstance(y, float)
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
            for obj in definingObjects:
                assert isinstance(obj, GeometricObject)
                obj.addChild(self)
                
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
    
    def setCoordinates(self, x, y):
        if self.free():
            self.x = x
            self.y = y
        return self.childObjects
        
    def getCoordinates(self):
        return self.x, self.y
    
    def exists(self):
        return self.doesExist

    def free(self):
        return self.isFree
    
    def distanceToPoint(self, point2):
        assert isinstance(point2, Point)
        x2, y2 = point2.getCoordinates()
        return distanceBetweenPoints(self.x, self.y, x2, y2)
    
    def getVisibility(self):
        return self.isVisible
    
    def __str__(self):
        x,y = self.getCoordinates()
        return f"Point ({x}, {y})"
    
    def setVisibility(self, isVisible):
        self.isVisible = isVisible

    def isClose(self, x, y, tolerance):
        return distanceBetweenPoints(self.x, self.y, x, y) <= tolerance
    
    def addChild(self, object):
        self.childObjects.append(object)



def distanceBetweenPoints(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5