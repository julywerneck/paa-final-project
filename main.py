from graphics import *
import random as rd
from Trapezium import Trapezium

"""
TODO :
    -> Arrumar bug que o trapezio fica um pouco maior que o outline do retangulo
    -> função desperdício de tecido
    -> função força bruta
"""

"""
Constantes
"""
TOP_Y = 20
BOTTOM_Y = 120
HEIGHT = 100

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
        p1 = Point(limT,TOP_Y - 1)
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

def getRandomColor():
    return color_rgb(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))

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

def Questao1(win):
    x1a, x2a, x3a = input().split(' ')
    x1b, x2b, x3b = input().split(' ')
    
    # Calculo primeiro trapezio
    poly = createPolygon(float(x1a), float(x2a), float(x3a), 0, 0)
    first_x = min(poly.getPoints()[0].getX(), poly.getPoints()[3].getX())
    poly.setFill(color_rgb(255,0,255))
    print("PRIMEIRO TRAPEZIO")
    print(poly.getPoints())
    limT = poly.getPoints()[1].getX() # P2 do trapezio
    limB = poly.getPoints()[2].getX() # p3 do trapezio
    print("LIMITE TOP " + str(limT))
    print("LIMITE BOTTOM " + str(limB))
    trap1 = Trapezium(poly) 
    
    
    # calcula segundo trapezio
    poly = createPolygon(float(x1b), float(x2b), float(x3b), limT, limB)
    last_x = max(poly.getPoints()[1].getX(), poly.getPoints()[2].getX())
    poly.setFill(getRandomColor())
    print("SEGUNDO TRAPEZIO")
    print(poly.getPoints())
    limT = poly.getPoints()[1].getX()
    limB = poly.getPoints()[2].getX()
    print("LIMITE TOP " + str(limT))
    print("LIMITE BOTTOM " + str(limB))
    trap2 = Trapezium(poly)
    
    # cria o tecido
    width = last_x - first_x
    print("LARGURA TECIDO "+str(width))
    rect = createRectangle(width, TOP_Y)
    rect.setOutline(color_rgb(0,100,0))
    rect.draw(win)
    win.flush()
    trap1.poly.draw(win)
    trap2.poly.draw(win)

    return 0


limT = 0
limB = 0

def main():
    
    # coords = readInput()

    win = GraphWin("My Window", 500, 500)
    # rect = createRectangle(500, 20)
    win.setBackground(color_rgb(0, 0, 0))
    # rect.setOutline(color_rgb(0, 100, 0))
    # rect.draw(win)
    
    Questao1(win)
    
    # poly = createPolygon(20, 20, 60, 20, 80, 120, 10, 120)
    # poly.setFill(color_rgb(255, 0, 255))
    # getRepresentations(poly)
    # poly.draw(win)
    
    win.getMouse()
    win.close()


main()
