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
        self.color = None

        self.label = None
        self.labelDirection = None
        self.labelDistance = 15
        self.labelIsVisible = True

        self.correctPosition()
    
    def correctPosition(self):
        if any([not obj.exists() for obj in self.definingObjects if isinstance(obj, GeometricObject)]):
            self.xCoef = None
            self.yCoef = None
            self.c = None
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
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setLabel(self, label):
        self.label = label

    def getLabel(self):
        return self.label

    def setLabelDirection(self, labelDirection):
        self.labelDirection = labelDirection

    def getLabelDirection(self):
        return self.labelDirection

    def setLabelDistance(self, labelDistance):
        self.labelDistance = labelDistance

    def getLabelDistance(self):
        return self.labelDistance

    def setLabelVisibility(self, isVisible):
        self.labelIsVisible = isVisible

    def getLabelVisibility(self):
        return self.labelIsVisible

    def getPlottingCoordinates(self, boundingBox):

        # There is a bug somewhere here. The line is not being plotted correctly when off canvas.

        a, b, c = self.getCoefficients()
        lowerx, lowery = boundingBox[0]
        upperx, uppery = boundingBox[1]

        lowerLinex, lowerLiney = self.getBoundaries()[0]
        upperLinex, upperLiney = self.getBoundaries()[1]

        if not lowerLinex is None:
            lowerx = max(lowerx, lowerLinex)
        if not lowerLiney is None:
            lowery = max(lowery, lowerLiney)
        if not upperLinex is None:
            upperx = min(upperx, upperLinex)
        if not upperLiney is None:
            uppery = min(uppery, upperLiney)
        
        if b == 0:
            x1 = c / a
            if not lowerx <= x1 <= upperx:
                return
            y1 = lowery
            y2 = uppery
            x2 = x1
            return x1, y1, x2, y2
        elif a == 0:
            y1= c / b
            if not lowery <= y1 <= uppery:
                return
            x1 = lowerx
            x2 = upperx
            y2 = y1 
            return x1, y1, x2, y2

        # Now a and b are both non-zero
        xPoints = []
        yPoints = []
        x = (c - b * lowery) / a
        if lowerx <= x <= upperx:
            xPoints.append(x)
            yPoints.append(lowery)
        x = (c - b * uppery) / a
        if lowerx <= x <= upperx:
            xPoints.append(x)
            yPoints.append(uppery)
        y = (c - a * lowerx) / b
        if lowery <= y <= uppery:
            xPoints.append(lowerx)
            yPoints.append(y)
        y = (c - a * upperx) / b
        if lowery <= y <= uppery:
            xPoints.append(upperx)
            yPoints.append(y)
        sortedxPoints = sorted(xPoints)
        x1, x2 = sortedxPoints[0], sortedxPoints[-1]
        y1 = yPoints[xPoints.index(x1)]
        y2 = yPoints[xPoints.index(x2)]
        return x1, y1, x2, y2

    def __str__(self):
        a, b, c = self.getCoefficients()
        return f"Line ({a:.2f}x + {b:.2f}y = {c:.2f})"