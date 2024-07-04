from Object import GeometricObject

class Point(GeometricObject):

    def __init__(self, x = None, y = None, definingObjects = None, 
                constructionStrategy = None, name = None, isVisible = False):

        if not definingObjects:
            self.isFree = True
            self.definingObjects = []
            self.constructionStrategy = None
            self.x = x
            self.y = y
            self.doesExist = True

        else:
            self.isFree = False
            self.definingObjects = definingObjects
            self.constructionStrategy = constructionStrategy
            self.x = 0
            self.y = 0
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
            if not self.isFree:
                self.x, self.y = self.constructionStrategy(self.definingObjects)
            if self.x == None or self.y == None:
                self.doesExist = False
            else:
                self.doesExist = True

        return self.childObjects
    
        
    def getCoordinates(self):
        return self.x, self.y
    
    def exists(self):
        return self.doesExist