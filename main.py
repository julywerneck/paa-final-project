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
Lê entrada de coordenadas
n : numero de elementos (trapezios)
coords[] : Lista de n elementos contendo x1, x2 e x3 
'''
def readInput():
    n = input() 
    coords = []
    for i in range(int(n)): 
        coords.append(input().split(' '))
    return coords

'''
TODO:
    - printar o poly B
    - cálculo do disperdício de tecido (?)
'''
def Questao1(rect,win):
    x1a, x2a, x3a = input().split(' ')
    # x1b, x2b, x3b = input().split(' ')
    
    if (float(x3a) > 0):
        poly = createPolygon(1, 20,
                             1+float(x1a), 20,
                             1+float(x3a)+float(x2a), 120,
                             1+float(x3a), 120) 
        poly.setFill(color_rgb(255,0,255))
        win.flush()
        poly.draw(win)
        
    return 0


def main():
    
    # coords = readInput()

    win = GraphWin("My Window", 500, 500)
    rect = createRectangle(500, 20)
    win.setBackground(color_rgb(0, 0, 0))
    rect.setOutline(color_rgb(0, 100, 0))
    rect.draw(win)
    
    # Questao1(rect,win)
    
    poly = createPolygon(20, 20, 60, 20, 80, 120, 10, 120)
    poly.setFill(color_rgb(255, 0, 255))
    getRepresentations(poly)
    poly.draw(win)
    win.getMouse()
    win.close()


main()
