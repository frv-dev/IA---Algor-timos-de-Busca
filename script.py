import numpy as np
from DTO.Node import Node
from DTO.MyList import MyList
from algorithms.getData import getData
from algorithms.verifyMatrix import verifyMatrix
from algorithms.amplitude import amplitude

if __name__ == '__main__':
    matrix, nodes = getData()
    print("> Dados capturados, matrix pronta")
    if not verifyMatrix(matrix, nodes):
        exit(0)
    print("> Matrix validada com sucesso")

    print("> Iniciando busca em amplitude")
    path = amplitude(matrix, nodes, 'A', 'D')
    newPath = [node for node in reversed(path)]
    print(newPath)
