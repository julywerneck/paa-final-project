from Tissue import Tissue 
from utils import *
from Trapezium import *


def heuristic(coords,win):
    tissue = Tissue(len(coords)) 
    tissue.calc_trapezium(coords[0])
    tissue.calc_trapezium(coords[1])
    # tissue.draw_tissue(win)
    tissue.remove_trapezium()
    tissue.draw_tissue(win)
    return 0