from Tissue import calc_permutations, calc_trapezoids, create_rectangle
from utils import *

"""
Algoritmo de Força bruta
@params: win -> tela do programa, coords -> lista de coordenadas recebidas
"""


def bruteForce(win, coords):
    desp = []  # desperdícios
    ordem = []  # ordem de peças
    widths = []  # larguras

    permuts = []
    for p in calc_permutations(coords):
        permuts.append(p)

    if DEBUG:
        print(f'LISTA DE PERMUTAÇÕES \n {permuts} ')

    for i in permuts:  # possibilidades
        d, o, w = calc_trapezoids(i)
        desp.append(d)
        ordem.append(o)
        widths.append(w)

    if DEBUG:
        print("desps")
        print(desp)
        print("widths")
        print(widths)
    index_best_order = desp.index(min(desp))
    print(f'MENOR DESPERDÍCIO DE TECIDO -->> {desp[index_best_order]}')
    rect = create_rectangle(widths[index_best_order], TOP_Y)
    rect.setOutline(VERDE)
    rect.draw(win)
    win.flush()
    for i in range(len(ordem[index_best_order])):
        ordem[index_best_order][i].poly.draw(win)

    return 0
