from Tissue import permutation, Tissue
from utils import *

"""
Algoritmo de Força bruta
@params: win -> tela do programa, coords -> lista de coordenadas recebidas
"""
def bruteForce(win, coords):
    n = len(coords)
    tissues = []

    permuts = []
    permutation(coords, n, permuts)  
    
    print(F'PERMUTAÇÕES GERADAS = {len(permuts)}')
    
    tissues.append(Tissue(n, permuts[0]))
    current_waste = tissues[0].waste
    index_best_order = 0

    if DEBUG:
        print(
            f'index = {0}, waste = {tissues[0].waste}, coords = {permuts[0]}')

    print('PERCORRENDO PERMUTAÇÕES')
    for x, i in enumerate(permuts[1:]):  # possibilidades
        tissues.append(Tissue(n, i))
        if DEBUG:
            print(
                f'index = {x+1}, waste = {tissues[x+1].waste}, coords = {permuts[x+1]}')
        if (tissues[x+1].waste < current_waste):
            current_waste = tissues[x + 1].waste
            index_best_order = x + 1

    print(
        f'MENOR DESPERDÍCIO DE TECIDO -->> {tissues[index_best_order].waste}')
    tissues[index_best_order].draw_tissue(win)

    return 0
