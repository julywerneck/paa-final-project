from graphics import *
from Tissue import *
from utils import *
from bruteForce import bruteForce
from branchAndBound import branch_and_bound
from heuristic import heuristic

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
    coords = read_input_from_file(str(input("Entre com o nome do arquivo :")))
    bruteForce(win, coords)
    return 0


def question_4(win):
    print("questao 4")
    coords = read_input_from_file(str(input("Entre com o nome do arquivo :")))
    branch_and_bound(win, coords)
    return 0


def question_5(win):
    print("questao 5")
    coords = read_input_from_file(str(input("Entre com o nome do arquivo :")))
    heuristic(coords, win)


def create_test_cases(win):
    coords = read_input_from_file(str(input("Entre com o nome do arquivo :")))
    tissue = Tissue(len(coords), coords)
    tissue.draw_tissue(win, True)
    print(f'LARGURA -> {tissue.width}')
    print(f'DESPERDICIO -> {tissue.waste}')
    return 0


def main():

    win = GraphWin("Trabalho de PAA", 600, 600)
    win.setBackground(color_rgb(0, 0, 0))
    op = int(input(
        "Opção -->> \n[Q01 = 0]\n[Q03(Força Bruta) = 1]\n[Q04(Branch and Bound) = 2]\n[Q05(Heurística) = 3]\n[TESTE = 4]\n : "))

    if op == 0:
        question_1(win)
    elif op == 1:
        question_3(win)
    elif op == 2:
        question_4(win)
    elif op == 3:
        question_5(win)
    elif op == 4:
        create_test_cases(win)

    win.getMouse()
    win.close()


main()


def menu():
    print(COLOR.HEADER+"=== Algoritmo de Tomasulo ==="+COLOR.ENDC)
    print("- Gustavo Torres Bretas Alves")
    print("- Maria Fernanda Oliveira Guimarães")
    print("- Maria Luiza Raso")
    print("- Rafael Lopes Murta")
    print("- Yan Silva Dumont")
    print(COLOR.OKBLUE+"=========== Configurações: ============"+COLOR.ENDC)

    debug = input("- Debug? (s/n) - Enter para não: ")
    status_avancado = input(
        "- Status avançado? [Mostrar Registradores e Celulas de Memoria] (s/n) - Enter para não: ")
    arquivo = input("- Arquivo de entrada? - Enter para o testes/input.txt: ")

    debug = debug.lower()
    status_avancado = status_avancado.lower()
    yes = ["s", "y", "sim", "yes"]

    if debug in yes:
        debug = True
    else:
        debug = False

    if status_avancado in yes:
        status_avancado = True
    else:
        status_avancado = False

    if(arquivo == ""):

        arquivo = "tomasulo-new/input.txt"

    try:
        inputFile = open(arquivo)
    except:
        print(COLOR.FAIL+"Arquivo de leitura não encontrado"+COLOR.ENDC)
        sys.exit()

    instrucoes = interpretador(inputFile)
    Tomasulo(instrucoes, debug, status_avancado).run()


# Função Main
def main():
    menu()


if __name__ == "__main__":
    main()
