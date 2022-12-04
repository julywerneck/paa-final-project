from Trapezium import *
from utils import *

'''
Calcula trapézios no tecido
@params:
    traps -> lista de coordenadas dos traps
@return:
    desperdício de tecido,
    ordem dos trapezios,
    largura necessária para atual ordem de peças
'''
def calc_trapezoids(traps):
    limT = 0
    limB = 0
    first_x = 0
    last_x = 0
    trap_order = []
    for i, x in enumerate(traps):
        x1, x2, x3 = x[0], x[1], x[2]
        t = Trapezium(float(x1), float(x2), float(x3), limT, limB)
        trap_order.append(t)
        if i == 0:
            first_x = min(t.poly.getPoints()[
                0].getX(), t.poly.getPoints()[3].getX())
        elif i == len(traps) - 1:
            last_x = max(t.poly.getPoints()[
                1].getX(), t.poly.getPoints()[2].getX())
        limT = t.poly.getPoints()[1].getX()
        limB = t.poly.getPoints()[2].getX()

    w = last_x - first_x
    return calc_waste(float(w*HEIGHT), trap_order), trap_order, w


"""
Calcula desperdício de tecido
@params: rect_area -> area do tecido utilizado
    traps -> lista contendo os trapezios no tecido
@return:
    area do tecido - area dos trapezios
"""
def calc_waste(rect_area, traps):
    area_traps = 0
    for i in traps:
        area_traps += i.get_area()

    return rect_area - area_traps


"""
Calcula todas as possíveis ordens das peças
@params:
    p -> lista de coordenadas 
@return:
    lista contendo todas as permutações
"""
def calc_permutations(p):
    if len(p) == 0:
        return []
    elif len(p) == 1:
        return [p]

    _p = []

    for i in range(len(p)):
        aux = p[i]
        resto_p = p[:i] + p[i+1:]
        for j in calc_permutations(resto_p):
            _p.append([aux] + j)

    return _p


'''
Cria retangulo com base na width e init das peças 
@params:
    width -> largura do retângulo
    init -> ponto de início 
@return:
    retângulo criado
'''
def create_rectangle(width, init):
    max_height = init + 100
    max_width = width - 1
    p1 = Point(max_width, max_height)
    p2 = Point(1, init)
    return Rectangle(p1, p2)


def insert_trapezium(lists, coords, limB, limT, first_x):
    x1, x2, x3 = coords[0], coords[1], coords[2]
    t = Trapezium(float(x1), float(x2), float(x3), limT, limB)
    lists.append(t)
    limT = t.poly.getPoints()[1].getX()
    limB = t.poly.getPoints()[2].getX()
    if len(lists) == 1:
        first_x = min(t.poly.getPoints()[
            0].getX(), t.poly.getPoints()[3].getX())
    last_x = max(t.poly.getPoints()[
        1].getX(), t.poly.getPoints()[2].getX())
    w = last_x - first_x
    waste = calc_waste(float(w*HEIGHT), lists)
    return limB, limT, waste, w, first_x, t
