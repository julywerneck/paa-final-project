from Tissue import Tissue
from utils import *

"""
Algoritmo de Força bruta
@params: win -> tela do programa, coords -> lista de coordenadas recebidas
"""
def permutation_brute_force(p, size, generated_p):
    if size == 1:
        generated_p.append(Tissue(0,p.copy()))
        return
        
    for i in range(size):
        permutation_brute_force(p,size-1,generated_p)
        
        if size % 2 == 1:
            p[0], p[size-1] = p[size-1], p[0]
        else:
            p[i], p[size-1] = p[size-1], p[i]


def bruteForce(win, coords):
    n = len(coords)
    tissues = []
    permutation_brute_force(coords,n,tissues)
    print(f'NUMERO DE PERMS GERADASS = {len(tissues)}')
    best_tissue = tissues[0] 
    for x,i in enumerate(tissues[1:]):
        if tissues[x+1].waste < best_tissue.waste:
            best_tissue = tissues[x+1] 
         
    print(f'MENOR DESPERDÍCIO DE TECIDO --->> {best_tissue.waste}')
    best_tissue.draw_tissue(win)
    return 0
