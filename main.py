from graphics import *
import random as rd
from Trapezium import Trapezium
from itertools import permutations

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


def getRepresentations(poly):
    topLenght = poly.getPoints()[1].getX() - poly.getPoints()[0].getX()
    print(topLenght)


"""
Calcula desperdício de tecido 
    rect_area -> area do tecido utilizado
    traps -> lista contendo os trapezios no tecido
    return <- area do tecido - area dos trapezios 
"""
def calcDesperdicio(rect_area, traps):
    area_traps = 0
    for i in traps:
        area_traps += i.getArea()
  
    return rect_area - area_traps

"""
Calcula todas as possíveis ordens das peças
"""
def calcPermutacoes(p):
   return permutations(p) 
    

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
    coords = []
    coords.append(input().split(' '))
    coords.append(input().split(' '))
    desp = []
    ordem = []
    widths = []
    
    permuts = calcPermutacoes(list(range(len(coords))))
    permuts = list(permuts)
    
    for i in permuts: # possibilidades
        limT = 0 
        limB = 0
        first_x = 0 
        last_x = 0 
        width = 0
        traps = []
        print(i)
        for index,j in enumerate(list(i)):# calcula os traps
            x1,x2,x3 = coords[j][0], coords[j][1], coords[j][2]
            # cria o trapezio
            traps.append( Trapezium(float(x1),float(x2),float(x3),limT, limB) ) 
            # define o primeiro e ultimo X do tecido
            if index == 0:
                first_x = min(traps[index].poly.getPoints()[0].getX(), traps[index].poly.getPoints()[3].getX()) 
            elif index == len(coords)-1:
                last_x = max(traps[index].poly.getPoints()[1].getX(), traps[index].poly.getPoints()[2].getX())
            # define os limites TOP e BOTTOM de X    
            limT = traps[index].poly.getPoints()[1].getX() 
            limB = traps[index].poly.getPoints()[2].getX() 
        width = last_x - first_x
        desp.append( calcDesperdicio(float(width*HEIGHT),traps))
        ordem.append(traps)
        widths.append(width)
    
    print("desps")
    print(desp)
    print("widths")
    print(widths)
    index_best_order = desp.index(min(desp))
    print("MENOR DESPERDÍCIO DE TECIDO -->>"+str(index_best_order))
    print(desp[index_best_order])
    rect = createRectangle(widths[index_best_order], TOP_Y)
    rect.setOutline(color_rgb(0,100,0))
    rect.draw(win)
    win.flush()
    for i in range(len(ordem[index_best_order])):
        ordem[index_best_order][i].poly.draw(win)
    return 0


limT = 0
limB = 0

def main():
    
    # coords = readInput()
    # a = list(range(len(coords)))
    # pl = calcPermutacoes(a)
    # print(list(pl))
        
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
