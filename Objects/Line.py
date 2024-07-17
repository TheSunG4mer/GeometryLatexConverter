import math
from Objects.Object import GeometricObject
from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy


class Line(GeometricObject):
    def __init__(self, definingObjects, constructionStrategy, name = None, isVisible = False):
        
        assert all([isinstance(obj, GeometricObject) for obj in definingObjects])
        assert isinstance(constructionStrategy, ConstructionStrategy)
        self.definingObjects = definingObjects
        for obj in definingObjects:
            obj.addChild(self)
        self.constructionStrategy = constructionStrategy

        self.xCoef = 1
        self.yCoef = 1
        self.c = 0
        self.doesExist = True
        self.boundaries  = [[None, None], # Used for halflines and line segments
                            [None, None]] # First list is lower x,y coordinates
                                          # Second is upper. None is \pm infinity depending on context.

        self.childObjects = []
        self.name = name
        self.isVisible = isVisible

        self.correctPosition()
    
    def correctPosition(self):
        if any([not obj.exists() for obj in self.definingObjects if isinstance(obj, GeometricObject)]):
            self.x = None
            self.y = None
            self.doesExist = False
        else:
            self.xCoef, self.yCoef, self.c, self.boundaries = self.constructionStrategy.constructObject(self.definingObjects)
            if self.xCoef == None or self.yCoef == None or self.c == None:
                self.doesExist = False
            else:
                self.doesExist = True

        return self.childObjects
        
    def getCoefficients(self):
        return self.xCoef, self.yCoef, self.c
    
    def getBoundaries(self):
        return self.boundaries

    def exists(self):
        return self.doesExist
    
    def isPointInBoundingBox(self, coordinates):
        x, y = coordinates
        lower, upper = self.getBoundaries()
        lowerx, lowery = lower
        upperx, uppery = upper
        if lowerx is not None:
            if lowerx > x:
                return False
        if lowery is not None:
            if lowery > y:
                return False
        if upperx is not None:
            if upperx < x:
                return False
        if uppery is not None:
            if uppery < y:
                return False
        return True
    
    def setVisibility(self, isVisible):
        self.isVisible = isVisible
    
    def getVisibility(self):
        return self.isVisible
    
    def distanceToPoint(self, x, y):
        a, b, c = self.getCoefficients()
        return abs((a * x + b * y - c) / (a ** 2 + b ** 2) ** 0.5)

    def isClose(self, x, y, tolerance):
        return self.isPointInBoundingBox((x, y)) and self.distanceToPoint(x, y) <= tolerance
    
    def addChild(self, object):
        self.childObjects.append(object)

    def __str__(self):
        a, b, c = self.getCoefficients()
        return f"Line ({a:.2f}x + {b:.2f}y = {c:.2f})"