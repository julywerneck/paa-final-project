from graphics import *
from Tissue import *
from utils import *
from bruteForce import bruteForce

"""
TODO :
    -> Arrumar bug que o trapezio fica um pouco maior que o outline do retangulo
    -> classe para atual ordem de peças (?)
"""


def question_1(win):
    coords = []
    coords.append(input().split(' '))
    coords.append(input().split(' '))
    bruteForce(win, coords)
    return 0


def question_3(win):
    print("question 3")
    coords = read_input_from_file()
    bruteForce(win, coords)
    return 0


def create_test_cases(win):
    coords = read_input_from_file(str(input("Entre com o nome do arquivo :")))
    d, o, w = calc_trapezoids(coords)
    if DEBUG:
        print(f'LARGURA -> {w}')
        print(f'DESPERDICIO -> {d}')
    rect = create_rectangle(w, TOP_Y)
    rect.setOutline(VERDE)
    rect.draw(win)
    for i in o:
        if DEBUG:
            print(f'AREA TRAPEZIO {i.getCoords()} == {i.getArea()}')
        i.poly.draw(win)
    return 0


def question_4():
    return 0


def main():

    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))
    op = int(input(
        "Opção -->> \n[Q01 = 0]\n[Q03 = 1]\n[Q04 = 2]\n[Q05 = 3]\n[TESTE = 4]\n : "))

    if op == 0:
        question_1(win)
    elif op == 1:
        question_3(win)
    elif op == 2:
        pass
    elif op == 3:
        question_4(win)
    elif op == 4:
        create_test_cases(win)

    win.getMouse()
    win.close()


main()
