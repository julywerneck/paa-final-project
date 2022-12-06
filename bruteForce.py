from Tissue import Tissue
from utils import *

"""
Algoritmo de Força bruta
@params: win -> tela do programa, coords -> lista de coordenadas recebidas
"""

def permutation_brute_force(p, size, generated_p, wastes):
    if size == 1:
        t = Tissue(p.copy())
        generated_p.append(t.coords_order.copy())
        wastes.append(t.waste)
        return
        
    for i in range(size):
        permutation_brute_force(p,size-1,generated_p,wastes)
        
        if size % 2 == 1:
            p[0], p[size-1] = p[size-1], p[0]
        else:
            p[i], p[size-1] = p[size-1], p[i]


def bruteForce(win, coords):
    n = len(coords)
    generated_coords = []
    generated_wastes = []
    
    permutation_brute_force(coords,n,generated_coords, generated_wastes)
    
    best_tissue_index = generated_wastes.index(min(generated_wastes))
    
    print(f'NUMERO DE PERMS GERADAS = {len(generated_coords)}')
    print(f'MENOR DESPERDÍCIO DE TECIDO --->> {generated_wastes[best_tissue_index]}')
    
    best_tissue = Tissue(generated_coords[best_tissue_index])
    best_tissue.draw_tissue(win)
    return 0
