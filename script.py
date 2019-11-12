import numpy as np
from DTO.Node import Node
from DTO.MyList import MyList
from algorithms.getData import getData
from algorithms.verifyMatrix import verifyMatrix
from algorithms.amplitude import amplitude
from algorithms.profundidade import profundidade
from algorithms.profundidade_limitada import profundidade_limitada
from algorithms.aprofundamento_iterativo import aprofundamento_iterativo
from algorithms.bidirecional import bidirecional

if __name__ == "__main__":
    matrix, nodes = getData()
    print("> Dados capturados, matrix pronta")
    if not verifyMatrix(matrix, nodes):
        exit(0)
    print("> Matrix validada com sucesso")

    print("> Iniciando busca em amplitude")
    path = amplitude(matrix, nodes, "A", "D")
    if type(path) == str:
        newPath = path
    else:
        newPath = [node for node in reversed(path)]
    print(newPath)

    print()

    print("> Iniciando busca em profundidade")
    path = profundidade(matrix, nodes, "A", "D")
    if type(path) == str:
        newPath = path
    else:
        newPath = [node for node in reversed(path)]
    print(newPath)

    print()

    print("> Iniciando busca em profundidade limitada")
    path = profundidade_limitada(matrix, nodes, "A", "D", 3)
    if type(path) == str:
        newPath = path
    else:
        newPath = [node for node in reversed(path)]
    print(newPath)

    print()

    print("> Iniciando busca em aprofundameto iterativo")
    path = aprofundamento_iterativo(matrix, nodes, "A", "D", 3)
    if type(path) == str:
        newPath = path
    else:
        newPath = [node for node in reversed(path)]
    print(newPath)

    print()

    print("> Iniciando busca bidirecional")
    path = bidirecional(matrix, nodes, "A", "D")
    print(path)
