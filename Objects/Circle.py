from Object import GeometricObject
from Point import Point

class Circle(GeometricObject):

    def __init__(self, definingObjects, constructionStrategy, name = None, isVisible = False):
        self.definingObjects = definingObjects
        self.constructionStrategy = constructionStrategy

        self.center = Point(x = 0, y = 0)
        self.radius = 1

        self.correctPosition()

        self.childObjects = []
        self.name = name
        self.isVisible = isVisible


    def correctPosition(self):
        if any([not obj.exists() for obj in self.definingObjects]):
            self.x = None
            self.y = None
            self.doesExist = False
        else:
            self.center, self.radius = self.constructionStrategy(self.definingObjects)
            if self.xCoef == None or self.yCoef == None or self.c == None:
                self.doesExist = False
            else:
                self.doesExist = True

        return self.childObjects


    def exists(self):
        return self.doesExist
    