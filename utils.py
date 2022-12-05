from graphics import color_rgb
from Color import COLOR
import sys

TOP_Y = 20
BOTTOM_Y = 120
HEIGHT = 100
VERDE = color_rgb(0, 100, 0)
DEBUG = False


def read_input_from_file(file=""):
    if file != "":
        path = "input/" + file
        arq = open(path)
    else:
        arq = open("input/in.txt")
    coords = []
    lines = [line.strip() for line in arq.readlines()]
    n = int(lines[0])
    for i in range(n):
        coords.append(lines[i+1].split(' '))
        verify_conditions(float(coords[i][0]), float(coords[i][1]), float(coords[i][2]))
    arq.close()
    return coords


def verify_conditions(x1,x2,x3):
    if x1 < 0:
        print(COLOR.FAIL+f'X1 NÃO PODE SER NEGATIVO [coords = {x1},{x2},{x3}]'+COLOR.FAIL)
        sys.exit()
    if x3 > x2:
        print(COLOR.FAIL+f'X3 NÃO PODE SER MAIOR QUE X2 [coords = {x1},{x2},{x3}]'+COLOR.FAIL)
        sys.exit()


def read_input():
    n = input()
    coords = []
    for i in range(int(n)):
        coords.append(input().split(' '))
    return coords
