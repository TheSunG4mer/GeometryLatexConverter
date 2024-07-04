from Object import GeometricObject

class Line(GeometricObject):
    def __init__(self, definingObjects, constructionStrategy, name = None, isVisible = False):
        self.definingObjects = definingObjects
        self.constructionStrategy = constructionStrategy

        self.xCoef = 1
        self.yCoef = 1
        self.c = 0
        self.doesExist = True

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
            self.xCoef, self.yCoef, self.c = self.constructionStrategy(self.definingObjects)
            if self.xCoef == None or self.yCoef == None or self.c == None:
                self.doesExist = False
            else:
                self.doesExist = True

        return self.childObjects
        

    def exists(self):
        return self.doesExist