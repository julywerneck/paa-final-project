from Tissue import calc_permutations, calc_trapezoids, create_rectangle, insert_trapezium_teste
from utils import *
from Trapezium import *

"""
Algoritmo de Força bruta
@params: win -> tela do programa, coords -> lista de coordenadas recebidas
"""


def find_best_trap(coords, minWaste, listResult, limB, limT, best):
    print("PRINT INICIO:", coords, listResult, limB, limT)
    if(coords == []):
        return True, listResult, minWaste
    else:
        for i in coords:
            toInsert = i
            _limB, _limT, waste = insert_trapezium_teste(
                listResult, toInsert, limB, limT)
            print(listResult, minWaste, waste)
            if waste <= minWaste:
                minWaste = waste
                find_best_trap(coords[1:], minWaste, listResult,
                               _limB, _limT, best)
            else:
                listResult.pop()
                find_best_trap(coords, minWaste, listResult,
                               limB, limT, best)


def branch_and_bound(win, coords):
    f, list_result, minWaste = find_best_trap(
        coords, 1000000, [], 0, 0, 3500)
    print(f'MENOR DESPERDÍCIO DE TECIDO -->> {minWaste}')
    rect = create_rectangle(200, TOP_Y)
    rect.setOutline(VERDE)
    rect.draw(win)
    win.flush()
    for i in range(len(list_result)):
        list_result[i].poly.draw(win)
    return 0
