from graphics import *
import random


"""
Constantes
"""
TOP_Y = 20
BOTTOM_Y = 120


"""
Cria Poligono
x1,x2,x3 -> coordenadas de entrada
limT -> coordenada limite de X TOP
    X superior direito do Poly 
    caso tecido vazio, 0
limB -> coordenada limite de X BOTTOM
    X inferior direito do Poly
    caso tecido vazio, 0
"""
def createPolygon(x1, x2, x3, limT, limB):
    if x3 > 0:
        p1 = Point(limT,TOP_Y)
        p2 = Point(p1.getX() + x1,TOP_Y)
        p4 = Point(limB + x3, BOTTOM_Y)
        p3 = Point(p4.getX() + x2, BOTTOM_Y)
    elif x3 < 0:
        x3 = abs(x3)
        p1 = Point(limT + x3, TOP_Y)
        p2 = Point(p1.getX() + x1,TOP_Y)
        p4 = Point(limB, BOTTOM_Y)
        p3 = Point(p4.getX() + x3 + x2, BOTTOM_Y)
    
    return Polygon(p1,p2,p3,p4)


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
    - cálculo do disperdício de tecido 
        area do retangulo - area dos polys
'''
def Questao1(rect,win):
    x1a, x2a, x3a = input().split(' ')
    # x1b, x2b, x3b = input().split(' ')
    
    poly = createPolygon(float(x1a), float(x2a), float(x3a), 0, 0) 
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
    
    Questao1(rect,win)
    
    # poly = createPolygon(20, 20, 60, 20, 80, 120, 10, 120)
    # poly.setFill(color_rgb(255, 0, 255))
    # getRepresentations(poly)
    # poly.draw(win)
    win.getMouse()
    win.close()


main()
