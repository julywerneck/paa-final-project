from graphics import *


def createPolygon(x1, x2, x3):
    return Polygon(Point(x1, y1), Point(x2, y2),
                   Point(x3, y3), Point(x4, y4))


def getRepresentations(poly):
    topLenght = poly.getPoints()[1].getX() - poly.getPoints()[0].getX()
    print(topLenght)


def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))

    poly = createPolygon(20, 20, 60, 20, 80, 120, 10, 120)
    poly.setFill(color_rgb(255, 0, 255))
    getRepresentations(poly)
    win.getMouse()
    win.close()


main()
