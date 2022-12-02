from graphics import *
import random as rd
from utils import *

class Trapezium():
    
    def __init__(self, x1,x2,x3,limT,limB):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        polygon = self.createPolygon(x1,x2,x3,limT,limB)
        polygon.setFill(self.getRandomColor())
        points = polygon.getPoints()
        self.poly = polygon
        self.baseT = points[1].getX() - points[0].getX() # base Top
        self.baseB = points[2].getX() - points[3].getX() # base Bottom
        
    
    def getCoords(self):
        return [self.x1,self.x2,self.x3]
    
    def getArea(self):
        return ( (self.baseB + self.baseT) * 100 ) / 2
    
    """
    Cria Poligono
        x1,x2,x3 -> coordenadas de entrada
        limT -> coordenada limite de X TOP
            X superior direito do Poly 
            caso tecido vazio, 0
        limB -> coordenada limite de X BOTTOM
            X inferior direito do Poly
            caso tecido vazio, 0
        return <- Polygono criado com o calculo dos pontos 1,2,3,4
    """
    def createPolygon(self, x1, x2, x3, limT, limB):
        if x3 > 0:
            p1 = Point(limT,TOP_Y)
            p2 = Point(p1.getX() + x1,TOP_Y)
            p4 = Point(p1.getX() + x3, BOTTOM_Y)
            p3 = Point(p4.getX() + x2, BOTTOM_Y)
        elif x3 < 0:
            x3 = abs(x3)
            p4 = Point(limB, BOTTOM_Y)
            p1 = Point(p4.getX() + x3, TOP_Y)
            p2 = Point(p1.getX() + x1,TOP_Y)
            p3 = Point(p4.getX() + x3 + x2, BOTTOM_Y)
        
        if DEBUG: 
            print(f'TRAPEZIO {self.getCoords()} -->> ')
            print(f'\tP1({p1.getX()},{p1.getY()})')
            print(f'\tP2({p2.getX()},{p2.getY()})')
            print(f'\tP3({p3.getX()},{p3.getY()})')
            print(f'\tP4({p4.getX()},{p4.getY()})')
             
        return Polygon(p1,p2,p3,p4)

    def getRandomColor(self):
        return color_rgb(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))

