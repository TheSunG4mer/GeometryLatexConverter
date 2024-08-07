from Objects.Object import GeometricObject
from Objects.Point import Point

from Objects.ConstructionStrategies.ConstructionStrategy import ConstructionStrategy


class Circle(GeometricObject):

    def __init__(self, definingObjects, constructionStrategy, name = None, isVisible = False):
        assert isinstance(constructionStrategy, ConstructionStrategy)
        self.definingObjects = definingObjects
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
    
    