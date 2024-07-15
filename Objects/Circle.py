import math
from Objects.Object import GeometricObject
from Objects.Point import Point

from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy


class Circle(GeometricObject):

    def __init__(self, definingObjects, constructionStrategy, name = None, isVisible = False):
        assert isinstance(constructionStrategy, ConstructionStrategy)
        self.definingObjects = definingObjects
        for obj in definingObjects:
            assert isinstance(obj, GeometricObject)
            obj.addChild(self)
        self.constructionStrategy = constructionStrategy

        self.center = Point(x = 0, y = 0)
        self.radius = 1

        self.childObjects = []
        self.name = name
        self.isVisible = isVisible

        self.correctPosition()



    def correctPosition(self):
        if any([not obj.exists() for obj in self.definingObjects if isinstance(obj, GeometricObject)]):
            self.center = None
            self.radius = None
            self.doesExist = False
        else:
            self.center, self.radius = self.constructionStrategy.constructObject(self.definingObjects)
            if self.center == None or self.radius == None:
                self.doesExist = False
            else:
                self.doesExist = True

        return self.childObjects

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius

    def exists(self):
        return self.doesExist
    
    def setVisibility(self, isVisible):
        self.isVisible = isVisible
    
    def getVisibility(self):
        return self.isVisible
    
    def distanceToPoint(self, x, y):
        x0, y0 = self.center
        r = self.radius
        return abs(r - distanceBetweenPoints(x0, y0, x, y))
    
    def isClose(self, x, y, tolerance):
        return self.distanceToPoint(x, y) <= tolerance
    
    def addChild(self, object):
        self.childObjects.append(object)


def distanceBetweenPoints(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5