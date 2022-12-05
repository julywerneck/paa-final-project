from Tissue import *
from utils import *
from Trapezium import *

"""
Algoritmo de Força bruta
@params: win -> tela do programa, coords -> lista de coordenadas recebidas
"""
resposta = 0
best_order = []


def find_best_trap(coords, tissue):
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
                find_best_trap(
                    coords, tissue)
                coords.append(element)
                tissue.remove_trapezium()


def branch_and_bound(win, coords):
    tissue = Tissue(3, coords)
    global resposta
    global best_order
    resposta = tissue.waste
    find_best_trap(
        coords, Tissue(3))
    print(f'MENOR DESPERDÍCIO DE TECIDO -->> {resposta}')
    print(best_order)
    tissue_final = Tissue(3, best_order)
    tissue_final.draw_tissue(win)
    return 0
