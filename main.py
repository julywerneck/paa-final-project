from graphics import *
from Trapezium import Trapezium
from utils import *

"""
TODO :
    -> Arrumar bug que o trapezio fica um pouco maior que o outline do retangulo
    -> classe para atual ordem de peças (?)
"""


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
    
    if len(p) == 0:
        return []
    elif len(p) == 1:
        return [p]
    
    _p = []
    
    for i in range(len(p)):
        aux = p[i] 
        resto_p = p[:i] + p[i+1:]
        for j in calcPermutacoes(resto_p):
            _p.append([aux] + j)
    
    return _p    

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
Calcula posição dos trapezios 
considerando um tecido vazio
    traps -> lista de coordenadas dos traps
    return <- desperdício de tecido, 
            ordem dos trapezios,
            largura necessária para atual ordem de peças
'''
def calcTrapezios(traps):
    limT = 0 
    limB = 0
    first_x = 0 
    last_x = 0 
    trap_order = []
    for i,x in enumerate(traps):
        x1,x2,x3 = x[0], x[1], x[2]
        t = Trapezium(float(x1),float(x2),float(x3),limT, limB)
        trap_order.append(t)
        if i == 0:
            first_x = min(t.poly.getPoints()[0].getX(), t.poly.getPoints()[3].getX()) 
        elif i == len(traps) - 1:
            last_x = max(t.poly.getPoints()[1].getX(), t.poly.getPoints()[2].getX())
        limT = t.poly.getPoints()[1].getX() 
        limB = t.poly.getPoints()[2].getX() 
        
    w = last_x - first_x
    return calcDesperdicio(float(w*HEIGHT),trap_order),trap_order,w

"""
Algoritmo de Força bruta
    win -> tela do programa
    coords -> lista de coordenadas recebidas
"""
def bruteForce(win,coords):
    desp = [] # desperdícios
    ordem = [] # ordem de peças
    widths = [] # larguras
    
    permuts = [] 
    for p in calcPermutacoes(coords):
        permuts.append(p)
        
    if DEBUG:
        print(f'LISTA DE PERMUTAÇÕES \n {permuts} ')
    
    for i in permuts: # possibilidades
        d,o,w = calcTrapezios(i)
        desp.append(d)
        ordem.append(o)
        widths.append(w)
    
    if DEBUG:    
        print("desps")
        print(desp)
        print("widths")
        print(widths)
    index_best_order = desp.index(min(desp))
    print(f'MENOR DESPERDÍCIO DE TECIDO -->> {desp[index_best_order]}')
    rect = createRectangle(widths[index_best_order], TOP_Y)
    rect.setOutline(VERDE)
    rect.draw(win)
    win.flush()
    for i in range(len(ordem[index_best_order])):
        ordem[index_best_order][i].poly.draw(win)
     
    return 0

def Questao1(win):
    coords = []
    coords.append(input().split(' '))
    coords.append(input().split(' '))
    bruteForce(win,coords)   
    return 0

def Questao3(win):
    print("QUESTAO 3")
    coords = readInputFromFile()
    bruteForce(win,coords)
    return 0

def MontarCasosTeste(win):
    coords = readInputFromFile(str(input("Entre com o nome do arquivo :")))
    d,o,w = calcTrapezios(coords)    
    if DEBUG:
        print(f'LARGURA -> {w}')
        print(f'DESPERDICIO -> {d}')
    rect = createRectangle(w,TOP_Y)
    rect.setOutline(VERDE)
    rect.draw(win)
    for i in o:
        if DEBUG:
            print(f'AREA TRAPEZIO {i.getCoords()} == {i.getArea()}')
        i.poly.draw(win)    
    return 0

def Questao4():
    return 0

def main():
    
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))
    op = int(input("Opção -->> \n[Q01 = 0]\n[Q03 = 1]\n[Q04 = 2]\n[Q05 = 3]\n[TESTE = 4]\n : "))
    
    if op == 0:
        Questao1(win) 
    elif op == 1:
        Questao3(win)
    elif op == 2:
       pass 
    elif op == 3:
        Questao4(win)
    elif op == 4:
        MontarCasosTeste(win)
    
    win.getMouse()
    win.close()


main()
