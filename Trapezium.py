from graphics import *
import random as rd
from utils import *


class Trapezium():

    def __init__(self, x1, x2, x3, limT, limB):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        polygon = self.create_polygon(x1, x2, x3, limT, limB)
        polygon.setFill(self.get_random_color())
        points = polygon.getPoints()
        self.poly = polygon
        self.baseT = points[1].getX() - points[0].getX()  # base Top
        self.baseB = points[2].getX() - points[3].getX()  # base Bottom

    def get_coords(self):
        return [self.x1, self.x2, self.x3]

    def get_area(self):
        return ((self.baseB + self.baseT) * HEIGHT) / 2

    """
    @params: x1, x2, x3 -> coordenadas de entrada
            limT -> coordenada limite de X TOP
            limB -> coordenada limite de X BOTTOM
    @return: Polygono criado com o calculo dos pontos 1,2,3,4
    """

    def create_polygon(self, x1, x2, x3, limT, limB):
        inc = (limT - limB)
        if x3 > 0:
            if (inc < 0) and (abs(inc) > x3):
                p4 = Point(limB, BOTTOM_Y)
                p1 = Point(p4.getX() - x3, TOP_Y)
            else:
                p1 = Point(limT, TOP_Y)
                p4 = Point(p1.getX() + x3, BOTTOM_Y)
            p2 = Point(p1.getX() + x1, TOP_Y)
            p3 = Point(p1.getX() + x2, BOTTOM_Y)
        elif x3 < 0:
            x3 = abs(x3)
            if x3 < (inc):
                p1 = Point(limT, TOP_Y)
                p4 = Point(p1.getX() - x3, BOTTOM_Y)
            else:
                p4 = Point(limB, BOTTOM_Y)
                p1 = Point(p4.getX() + x3, TOP_Y)
            p2 = Point(p1.getX() + x1, TOP_Y)
            p3 = Point(p1.getX() + x2, BOTTOM_Y)

        if DEBUG:
            print(f'\tTRAPEZIO {self.get_coords()} -->> ')
            print(f'\t\tP1({p1.getX()},{p1.getY()})')
            print(f'\t\tP2({p2.getX()},{p2.getY()})')
            print(f'\t\tP3({p3.getX()},{p3.getY()})')
            print(f'\t\tP4({p4.getX()},{p4.getY()})')

        return Polygon(p1, p2, p3, p4)

    def get_random_color(self):
        return color_rgb(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
