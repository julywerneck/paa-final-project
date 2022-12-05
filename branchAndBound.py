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
best_order = []


def find_best_trap_new(coords, tissue):
    global resposta
    global best_order

    if(coords == []):
        if tissue.waste < resposta:
            best_order = []
            resposta = tissue.waste
            for i in tissue.trap_order:
                best_order.append(i.get_coords())
            return
    else:
        if(resposta >= tissue.waste):
            for i in range(len(coords)):
                element = coords.pop(0)
                tissue.calc_trapezium(element)
                find_best_trap_new(
                    coords, tissue)
                coords.append(element)
                tissue.remove_trapezium()


def branch_and_bound(win, coords):
    tissue = Tissue(3, coords)
    global resposta
    global best_order
    resposta = tissue.waste
    find_best_trap_new(
        coords, Tissue(3))
    print(f'MENOR DESPERDÍCIO DE TECIDO -->> {resposta}')
    print(best_order)
    tissue_final = Tissue(3, best_order)
    tissue_final.draw_tissue(win)
    return 0
