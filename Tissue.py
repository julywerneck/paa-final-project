from Trapezium import *
from utils import *

class Tissue():
    
    def __init__(self,n,coords=[]):
        self.n = n
        self.limT = 0
        self.limB = 0
        self.first_x = 0
        self.last_x = 0
        self.waste = 0
        self.width = 0
        self.trap_order = []
        if coords:
            self.calc_trapezoids(coords)
    

    def insert_trapezium(self,trap):
        if len(self.trap_order) == 0:
            self.first_x = min(trap.poly.getPoints()[0].getX(), trap.poly.getPoints()[3].getX())
        self.last_x = max(trap.poly.getPoints()[1].getX(), trap.poly.getPoints()[2].getX())
        self.trap_order.append(trap)
        self.limT = trap.poly.getPoints()[1].getX()
        self.limB = trap.poly.getPoints()[2].getX()
    
    
    '''
    Remove o ultimo trapezio inserido no tecido
    '''
    def remove_trapezium(self):
        self.trap_order.pop()
        last_trap = self.trap_order[len(self.trap_order) - 1]
        self.limT = last_trap.poly.getPoints()[1].getX() 
        self.limB = last_trap.poly.getPoints()[2].getX() 
        self.last_x = max(last_trap.poly.getPoints()[1].getX(), last_trap.poly.getPoints()[2].getX())
        self.calc_waste()
    
    '''
    Calcula desperdício atual do tecido
    ''' 
    def calc_waste(self):
        self.width = self.last_x - self.first_x
        area_traps = 0
        for i in self.trap_order:
            area_traps += i.get_area()
        rect_area = self.width * HEIGHT
        if DEBUG:
            print(f'\twidth -> {self.width}, rect_area -> {rect_area}, area_traps -> {area_traps} ')
            print(f'\twaste -> {rect_area - area_traps}')
            print(20*'=')
        self.waste = rect_area - area_traps
    
    
    '''
    Insere um único trapézio no tecido
    ''' 
    def calc_trapezium(self,coord):
        x1,x2,x3 = coord[0],coord[1],coord[2]
        t = Trapezium(float(x1), float(x2), float(x3), self.limT, self.limB)
        self.insert_trapezium(t)
        self.calc_waste()
    
    
    '''
    Insere n trapézios no tecido
    '''
    def calc_trapezoids(self,coords):
        if DEBUG:
            print(f'COORDS -> {coords}')
        for i,x in enumerate(coords):
            x1,x2,x3 = x[0], x[1], x[2]
            t = Trapezium(float(x1), float(x2), float(x3), self.limT, self.limB)
            self.insert_trapezium(t)
            self.calc_waste()
            
    '''
    Mostrar na tela ordem de tecidos atual
    ''' 
    def draw_tissue(self, win, is_teste = False):
        rect = create_rectangle(self.width, TOP_Y)
        rect.setOutline(VERDE)
        rect.draw(win)
        win.flush()
        for i in self.trap_order:
            if is_teste:
                print(f'AREA TRAPEZIO {i.get_coords()} == {i.get_area()}')
            i.poly.draw(win)
        
            
        
"""
Calcula desperdício de tecido
@params: rect_area -> area do tecido utilizado
    traps -> lista contendo os trapezios no tecido
@return:
    area do tecido - area dos trapezios
"""
def calc_waste(rect_area, traps):
    area_traps = 0
    for i in traps:
        area_traps += i.get_area()

    return rect_area - area_traps


"""
Calcula todas as possíveis ordens das peças
@params:
    p -> lista de coordenadas 
@return:
    lista contendo todas as permutações
"""
def calc_permutations(p):
    if len(p) == 0:
        return []
    elif len(p) == 1:
        return [p]

    _p = []

    for i in range(len(p)):
        aux = p[i]
        resto_p = p[:i] + p[i+1:]
        for j in calc_permutations(resto_p):
            _p.append([aux] + j)

    return _p


'''
Cria retangulo com base na width e init das peças 
@params:
    width -> largura do retângulo
    init -> ponto de início 
@return:
    retângulo criado
'''
def create_rectangle(width, init):
    max_height = init + 100
    max_width = width - 1
    p1 = Point(max_width, max_height)
    p2 = Point(1, init)
    return Rectangle(p1, p2)


def insert_trapezium(lists, coords, limB, limT, first_x):
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))
    x1, x2, x3 = coords[0], coords[1], coords[2]
    t = Trapezium(float(x1), float(x2), float(x3), limT, limB)
    lists.append(t)
    limT = t.poly.getPoints()[1].getX()
    limB = t.poly.getPoints()[2].getX()
    if len(lists) == 1:
        first_x = min(t.poly.getPoints()[
            0].getX(), t.poly.getPoints()[3].getX())
    last_x = max(t.poly.getPoints()[
        1].getX(), t.poly.getPoints()[2].getX())
    for i in lists:
        i.poly.draw(win)
    win.getMouse()
    win.close()
    w = last_x - first_x
    waste = calc_waste(float(w*HEIGHT), lists)
    return limB, limT, waste, w, first_x

def insert_trapezium_teste(lists, coords, limB, limT):
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))
    x1, x2, x3 = coords[0], coords[1], coords[2]
    t = Trapezium(float(x1), float(x2), float(x3), limT, limB)
    lists.append(t)
    limT = t.poly.getPoints()[1].getX()
    limB = t.poly.getPoints()[2].getX()
    for i in lists:
        i.poly.draw(win)
    win.getMouse()
    win.close()

    waste = calc_waste(float(210*HEIGHT), lists)
    return limB, limT, waste
