from Tissue import *
from utils import *
from Trapezium import *

"""
Algoritmo de branch and bound
@params: win -> tela do programa, coords -> lista de coordenadas recebidas
"""

best_waste = float('inf')
best_order = []
podas = 0


def find_best_trap(coords, tissue):
    global best_waste
    global best_order
    global podas
    global z

    if(len(coords) == 1):
        element = coords[0]
        tissue.calc_trapezium(element)
        if tissue.waste < best_waste:
            best_order = []
            best_waste = tissue.waste
            for i in tissue.trap_order:
                best_order.append(i.get_coords())
        return
    else:
        for i in range(len(coords)):
            n = 0 if len(coords) % 2 == 1 else i
            print(coords, i)
            element = coords.pop(n)
            tissue.calc_trapezium(element)
            if(best_waste > tissue.waste):
                find_best_trap(
                    coords, tissue)
            else:
                podas += 1
            coords.append(element)
            tissue.remove_trapezium()


def branch_and_bound(win, coords):
    global best_waste
    global best_order
    print(coords)
    find_best_trap(
        coords, Tissue())
    print(f'MENOR DESPERDÍCIO DE TECIDO -->> {best_waste}')
    print(f'QUANTIDADE DE RAMOS PODADOS -->> {podas}')
    tissue_final = Tissue(best_order)
    tissue_final.draw_tissue(win)

    return 0
