from Tissue import *
from utils import *
from Trapezium import *

"""
Algoritmo de Força bruta
@params: win -> tela do programa, coords -> lista de coordenadas recebidas
"""
best_waste = 0
best_order = []
podas = 0

def find_best_trap(coords, tissue):
    global best_waste
    global best_order
    global podas
    
    if(coords == []):
        print(tissue.waste, best_waste)
        if tissue.waste < best_waste:
            best_order = []
            best_waste = tissue.waste
            for i in tissue.trap_order:
                best_order.append(i.get_coords())
            return
    else:
        if(best_waste > tissue.waste):  # critério de poda
            for i in range(len(coords)):
                element = coords.pop(0)
                tissue.calc_trapezium(element)
                find_best_trap(
                    coords, tissue)
                coords.append(element)
                tissue.remove_trapezium()
        else:
            podas += 1


def branch_and_bound(win, coords):
    tissue = Tissue(coords)
    global best_waste
    global best_order
    best_waste = tissue.waste
    best_order = tissue.coords_order
    find_best_trap(
        coords, Tissue())
    print(f'MENOR DESPERDÍCIO DE TECIDO -->> {best_waste}')
    print(f'QUANTIDADE DE RAMOS PODADOS --->> {podas}')
    print(best_order)
    tissue_final = Tissue(best_order)
    tissue_final.draw_tissue(win)
    return 0
