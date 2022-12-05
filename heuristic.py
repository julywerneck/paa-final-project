from Tissue import Tissue 
from utils import *
from Trapezium import *

INC_ESQ = 0
INC_DIR = 1

'''
se x3 positivo e x1 > (x2 + x3)
	\
senao se x1 < (x2+x3)
	/

se x3 negativo e (|x3| + x1) > (|x3|+x2)
	/
senao se (|x3| + x1) < (|x3|+x2)
	\
'''
def define_inclination(x1,x2,x3):
    if x3 > 0:
        if x1 > (x2 + x3):
            return INC_DIR 
        elif x1 < (x2 + x3):
            return INC_ESQ 
        else:
            return -1
    elif x3 < 0:
        _x3 = abs(x3) 
        if (_x3 + x1) > (_x3 + x2):
            return INC_DIR
        elif (_x3 + x1) < (_x3 + x2):
            return INC_ESQ
        else: 
            return -1 
    


def permutation(p, size, generated_p):
    if size == 1:
        return
        
    for i in range(size):
        permutation(p,size-1,generated_p)
        
        if size % 2 == 1:
            p[0], p[size-1] = p[size-1], p[0]
        else:
            p[i], p[size-1] = p[size-1], p[i]



def heuristic(coords,win):
    coords_inc = []
    for x,i in enumerate(coords):
        coords_inc.append([define_inclination(float(i[0]),float(i[1]),float(i[2]))])
        print(f'COORDS = {i}, INC = {coords_inc[x]}')
    
    return 0