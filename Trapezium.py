from graphics import *

class Trapezium():
    
    def __init__(self, polygon):
        points = polygon.getPoints()
        self.poly = polygon
        self.baseT = points[1].getX() - points[0].getX() # base Top
        self.baseB = points[2].getX() - points[3].getX() # base Bottom
        print("BASE T " + str(self.baseT))
        print("BASE B " + str(self.baseB))
        
    def getWidthNeeded(self):
        return max(self.baseB, self.baseT)
    
    def getArea(self):
        return ( (self.baseB + self.baseT) * 100 ) / 2
    
    