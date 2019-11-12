import numpy as np
from DTO.MyList import MyList


def profundidade_limitada(matrix: np.ndarray, nodes: list, start, end, limit):
    myList_1 = MyList()
    myList_2 = MyList()
    visited = list()

    myList_1.insertAtBack(None, start, 0)
    myList_2.insertAtBack(None, start, 0)
    line = list()
    line.append(start)
    line.append(0)
    visited.append(line)

    while myList_1.isEmpty() is not True:
        actual = myList_1.deleteLast()
        if actual is None:
            break
        if actual.secondValue < limit:
            index = nodes.index(actual.firstValue)
            for count_1 in range(len(matrix[index]) - 1, -1, -1):
                if matrix[index][count_1]:
                    newValue = nodes[count_1]
                else:
                    continue
                flag = True
                for count_2 in range(len(visited)):
                    if visited[count_2][0] == newValue:
                        if visited[count_2][1] <= (actual.secondValue + 1):
                            flag = False
                        else:
                            visited[count_2][1] = actual.secondValue + 1
                        break
                if flag:
                    myList_1.insertAtBack(actual, newValue, actual.secondValue + 1)
                    myList_2.insertAtBack(actual, newValue, actual.secondValue + 1)
                    line = list()
                    line.append(newValue)
                    line.append(actual.secondValue + 1)
                    visited.append(line)
                    if newValue == end:
                        path = []
                        path = myList_2.getTree()
                        return path

    return "Caminho não encontrado com o limite " + str(limit)
