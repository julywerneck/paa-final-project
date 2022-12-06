from Tissue import Tissue 
from utils import *
from Trapezium import *

def define_inclination(x1,x2,x3):
    if x3 > 0:
        if x1 > (x2 + x3):
            return INC_RIGHT 
        elif x1 < (x2 + x3):
            return INC_LEFT 
        else:
            return -1
    elif x3 < 0:
        _x3 = abs(x3) 
        if (_x3 + x1) > (_x3 + x2):
            return INC_RIGHT 
        elif (_x3 + x1) < (_x3 + x2):
            return INC_LEFT
        else: 
            return -1 
    


z = 0
def permutation_heuristic(p, size, generated_p, wastes):
    global z
    if size == 1:
        t = Tissue(p.copy())
        generated_p.append(t.coords_order.copy())
        wastes.append(t.waste)
        return
        
    for i in range(size):
        permutation_heuristic(p,size-1,generated_p,wastes)
        
        if size % 2 == 1:
            p[0], p[size-1] = p[size-1], p[0]
        else:
            p[i], p[size-1] = p[size-1], p[i]

def define_inclination_esq(coord):
    return define_inclination(float(coord[0]), float(coord[1]), float(coord[2])) == INC_LEFT

def define_inclination_dir(coord):
    return define_inclination(float(coord[0]), float(coord[1]), float(coord[2])) == INC_RIGHT 


def heuristic_dir_esq(coords,win):
    coords_inc_dir = list(filter(define_inclination_dir, coords))
    coords_inc_esq = list(filter(define_inclination_esq, coords))
    
    best_order_dir = [] 
    best_wastes_dir = []
    best_order_esq = [] 
    best_wastes_esq = []
    
    permutation_heuristic(coords_inc_dir, len(coords_inc_dir), best_order_dir, best_wastes_dir)
    permutation_heuristic(coords_inc_esq, len(coords_inc_esq), best_order_esq, best_wastes_esq)
    
    index_best_order_dir = best_wastes_dir.index(min(best_wastes_dir))
    index_best_order_esq = best_wastes_esq.index(min(best_wastes_esq))
    final_best_order = best_order_dir[index_best_order_dir] + best_order_esq[index_best_order_esq] 
    
    final_tissue = Tissue(0,final_best_order)
    print(f'MELHOR DESPERDÍCIO DE TECIDO -->> {final_tissue.waste}')
    final_tissue.draw_tissue(win)
    return 0


def heuristic_minwaste(coords,win):
    tissue = Tissue()
    
    
    
    return 0

def heuristic(coords,win):
    heuristic_dir_esq(coords,win)