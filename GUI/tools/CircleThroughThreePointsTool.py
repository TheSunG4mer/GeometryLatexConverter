from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.Circle import Circle
from Objects.ConstructionStrategies.CircleThroughThreePointsConstruction import CircleThroughThreePointsConstruction
from Objects.ConstructionStrategies.GeocenterConstruction import GeocenterConstruction
from Objects.Point import Point


class CircleThroughThreePointsTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [3,0,0]
    
    def __str__(self):
        return "Circum Center Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects = [points[0], points[1], points[2]]

        circle = Circle(definingObjects=definingObjects, constructionStrategy=CircleThroughThreePointsConstruction(), isVisible=True)
        self.root.addObject(circle)
        self.root.redraw()

