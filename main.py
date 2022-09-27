from graphics import *
import random


def createPolygon(x1, y1, x2, y2, x3, y3, x4, y4):
    return Polygon(Point(x1, y1), Point(x2, y2),
                   Point(x3, y3), Point(x4, y4))


def getRepresentations(poly):
    topLenght = poly.getPoints()[1].getX() - poly.getPoints()[0].getX()
    print(topLenght)


'''
Cria retangulo no centro da tela
com base na width e init das peças 
'''


def createRectangle(width, init):
    max_height = init + 100
    max_width = width - 1
    p1 = Point(max_width, max_height)
    p2 = Point(1, init)
    return Rectangle(p1, p2)


'''
TODO :
-> gerar cor rgb randomica
'''


def randomRGBColor():
    return color_rgb()


def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))

    rect = createRectangle(500, 20)
    rect.setOutline(color_rgb(0, 100, 0))
    rect.draw(win)

    poly = createPolygon(20, 20, 60, 20, 80, 120, 10, 120)
    poly.setFill(color_rgb(255, 0, 255))
    getRepresentations(poly)
    poly.draw(win)
    win.getMouse()
    win.close()


main()
