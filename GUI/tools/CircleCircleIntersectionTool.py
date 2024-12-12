



from GUI.tools.ObjectFromOtherObjectTool import ObjectFromOtherObjectTool
from Objects.ConstructionStrategies.PointAsCircleCircleIntersectionConstruction import PointAsCircleCircleIntersectionConstruction

from Objects.Point import Point


class CircleCircleIntersectionTool(ObjectFromOtherObjectTool):
    def __init__(self, root):
        super().__init__(root)
        self.requiredObjects = [0,0,2]
    
    def __str__(self):
        return "Circle-Circle Intersection Tool"
    
    def createObject(self):
        points, lines, circles = self.root.getSelectedSortedObjects()
        definingObjects1 = [circles[0], circles[1], 0]
        definingObjects2 = [circles[0], circles[1], 1]

        point1 = Point(definingObjects=definingObjects1, constructionStrategy=PointAsCircleCircleIntersectionConstruction(), isVisible=True)
        point2 = Point(definingObjects=definingObjects2, constructionStrategy=PointAsCircleCircleIntersectionConstruction(), isVisible=True)
        self.root.addObject(point1)
        self.root.addObject(point2)
        self.root.redraw()