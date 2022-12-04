from Tissue import create_rectangle, insert_trapezium
from utils import *
from Trapezium import *

"""
Algoritmo de Força bruta
@params: win -> tela do programa, coords -> lista de coordenadas recebidas
"""

def find_best_trap(coords, minWaste, listResult, limB, limT, first_x, w):
    if(len(coords) == 0):
        return True, listResult, minWaste, w
    else:
        toInsert = coords.pop(0)
        _limB, _limT, waste, _w, _first_x  = insert_trapezium(
            listResult, toInsert, limB, limT, first_x)
        if waste < minWaste:
            minWaste = waste
            found, result, best_waste, final_width = find_best_trap(coords, minWaste, listResult,
                                                                    _limB, _limT, _first_x, _w)
            if found:
                return found, result, best_waste, final_width
        else:
            coords.append(toInsert)
            found, result, best_waste, final_width = find_best_trap(coords, minWaste, listResult,
                                                                    limB, limT, first_x, w)
            if found:
                return found, result, best_waste, final_width


def branch_and_bound(win, coords):
    f, list_result, minWaste, w = find_best_trap(
        coords, 1000000, [], 0, 0, 0, w)
    print(f'MENOR DESPERDÍCIO DE TECIDO -->> {minWaste}')
    rect = create_rectangle(200, TOP_Y)
    rect.setOutline(VERDE)
    rect.draw(win)
    win.flush()
    for i in range(len(list_result)):
        list_result[i].poly.draw(win)
    return 0
