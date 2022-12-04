from Tissue import *
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
        _limB, _limT, waste, _w, _first_x = insert_trapezium(
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


def find_best_trap_new(coords, min_waste, tissue):
    if(coords == []):
        return True, min_waste, tissue
    else:
        for i in range(len(coords)):
            print(i)
            element = coords.pop(0)
            tissue.calc_trapezium(element)
            if(tissue.waste <= min_waste):
                min_waste = tissue.waste
                f, waste, tissue = find_best_trap_new(
                    coords.copy(), 100000, tissue)
                if f:
                    min_waste = waste
            else:
                tissue.remove_trapezium()
                f, waste, tissue = find_best_trap_new(
                    coords.copy(), min_waste, tissue)
                if f:
                    min_waste = waste
        return False, min_waste, tissue


def branch_and_bound(win, coords):
    f, minWaste, tissue = find_best_trap_new(
        coords, 1000000, Tissue(3))
    print(f'MENOR DESPERDÍCIO DE TECIDO -->> {minWaste}')
    tissue.draw_tissue(win)
    return 0
