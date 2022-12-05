from Tissue import *
from utils import *
from Trapezium import *

"""
Algoritmo de Força bruta
@params: win -> tela do programa, coords -> lista de coordenadas recebidas
"""


def find_best_trap(coords, min_waste, tissue):
    if(len(coords) == 0):
        return min_waste, tissue
    else:
        for coord in coords:
            element = coord
            tissue.calc_trapezium(element)
            if(tissue.waste <= min_waste):
                pass


resposta = 0
tissue_final = Tissue(3)


def find_best_trap_new(coords, min_waste, tissue):
    global resposta
    global tissue_final
    if(coords == []):
        print("entrei no if")
        if min_waste < resposta:
            resposta = min_waste
            tissue_final = tissue
            return
    else:
        if(resposta >= min_waste):
            print("entrei if")
            for i in range(len(coords)):
                element = coords.pop(0)
                tissue.calc_trapezium(element)
                find_best_trap_new(coords, min_waste, tissue)
                coords.insert(0, element)
                tissue.remove_trapezium()


def branch_and_bound(win, coords):
    tissue = Tissue(3, coords)
    resposta = tissue.waste
    find_best_trap_new(
        coords, tissue.waste, Tissue(3))
    print(f'MENOR DESPERDÍCIO DE TECIDO -->> {resposta}')
    tissue_final.draw_tissue(win)
    return 0
