from graphics import color_rgb


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
    for i in lines[1:]:
        coords.append(i.split(' '))
    arq.close()
    return coords


def read_input():
    n = input()
    coords = []
    for i in range(int(n)):
        coords.append(input().split(' '))
    return coords
