

from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.Circle import Circle
from Objects.ConstructionStrategies.CircleWithCenterAndPointConstruction import CircleWithCenterAndPointConstruction
from Objects.ConstructionStrategies.CircleWithCenterAndRadiusConstruction import CircleWithCenterAndRadiusConstruction


class CircleFromCenterAndPointTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [2, 0, 0]
    
    def __str__(self):
        return "Circle From Center And Point Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1]]
        circle = Circle(definingObjects=definingObjects, constructionStrategy= CircleWithCenterAndPointConstruction(), isVisible=True)
        self.root.addObject(circle)
        self.root.redraw()