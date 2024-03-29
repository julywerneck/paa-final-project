'''
July Ferreira Murta Werneck - 683595
Sofia Franca Campos Bhering - 665173
Thiago Amado Costa - 655537
'''

from graphics import *
from Tissue import *
from utils import *
from bruteForce import bruteForce
from branchAndBound import branch_and_bound
from heuristic import heuristic
from Color import COLOR
import time


def question_1(win):
    coords = []
    coords.append(input().split(' '))
    coords.append(input().split(' '))
    start = time.time()
    bruteForce(win, coords)
    return (time.time() - start)


def question_3(win):
    print("question 3")
    coords = read_input_from_file(str(input("Entre com o nome do arquivo :")))
    start = time.time()
    bruteForce(win, coords)
    return (time.time() - start)


def question_4(win):
    print(COLOR.OKBLUE+"\n[ INICIO BRANCH AND BOUND ]\n"+COLOR.ENDC)
    coords = read_input_from_file(str(input("Entre com o nome do arquivo :")))
    start = time.time()
    branch_and_bound(win, coords)
    print(COLOR.OKBLUE+f"TEMPO DE EXECUCAO: {time.time() - start}"+COLOR.ENDC)
    return (time.time() - start)


def question_5(win):
    print("questao 5")
    coords = read_input_from_file(str(input("Entre com o nome do arquivo :")))
    start = time.time()
    heuristic(coords, win)
    return (time.time() - start)


def create_test_cases(win):
    coords = read_input_from_file(str(input("Entre com o nome do arquivo :")))
    tissue = Tissue(coords)
    tissue.draw_tissue(win, True)
    print(f'LARGURA -> {tissue.width}')
    print(f'DESPERDICIO -> {tissue.waste}')
    return 0


def menu():
    win = GraphWin("Trabalho de PAA", 1280, 600)
    win.setBackground(color_rgb(0, 0, 0))
    print(COLOR.HEADER+"=== TRABALHO FINAL PAA ==="+COLOR.ENDC)
    print("- July Ferreira Murta Werneck")
    print("- Sofia Franca Campos Bhering")
    print("- Thiago Amado Costa\n")
    print(COLOR.OKGREEN+"TECNICA PARA EXECUCAO ====="+COLOR.ENDC)
    teste_string = (COLOR.FAIL+"[Teste = 4]"+COLOR.ENDC)
    print("[Força Bruta = 1]\n[Branch and Bound = 2]\n[Heurística = 3]\n"+teste_string+"\n")
    input_string = (COLOR.BOLD+"SUA ESCOLHA: "+COLOR.ENDC)
    op = int(input(input_string))

    if op == 0:
        question_1(win)
    elif op == 1:
        time = question_3(win)
        print("--- %.4f seconds ---" % time)
    elif op == 2:
        time = question_4(win)
        print("--- %.4f seconds ---" % time)
    elif op == 3:
        time = question_5(win)
        print("--- %.4f seconds ---" % time)
    elif op == 4:
        create_test_cases(win)

    win.getMouse()
    win.close()


def main():
    menu()


if __name__ == "__main__":
    main()
