import numpy as np
from DTO.MyList import MyList


def bidirecional(matrix: np.ndarray, nodes: list, start, end):
    myList_1 = MyList()
    myList_2 = MyList()
    myList_3 = MyList()
    myList_4 = MyList()
    visited = list()

    myList_1.insertAtBack(None, start, 0)
    myList_2.insertAtBack(None, start, 0)
    line = list()
    line.append(start)
    line.append(1)
    visited.append(line)

    myList_3.insertAtBack(None, end, 0)
    myList_4.insertAtBack(None, end, 0)
    line = list()
    line.append(end)
    line.append(2)
    visited.append(line)

    while True:
        flag_1 = True
        while flag_1:
            actual = myList_1.deleteFirst()
            index = nodes.index(actual.firstValue)
            for count_1 in range(len(matrix[index])):
                if matrix[index][count_1]:
                    newValue = nodes[count_1]
                else:
                    continue
                flag_2 = True
                flag_3 = False
                for count_2 in range(len(visited)):
                    if visited[count_2][0] == newValue:
                        if visited[count_2][1] == 1:
                            flag_2 = False
                        else:
                            flag_3 = True
                        break
                if flag_2:
                    myList_1.insertAtBack(actual, newValue, actual.secondValue + 1)
                    myList_2.insertAtBack(actual, newValue, actual.secondValue + 1)
                    if flag_3:
                        path = list()
                        path = myList_2.getTree()
                        path = path[::-1]
                        path += myList_4.getTree1(newValue)
                        return path
                    else:
                        line = list()
                        line.append(newValue)
                        line.append(1)
                        visited.append(line)

            if myList_1.isEmpty() != True:
                aux = myList_1.first()
                if aux.secondValue == actual.secondValue:
                    flag_1 = True
                else:
                    flag_1 = False

        flag_1 = True
        while flag_1:
            actual = myList_3.deleteFirst()
            index = nodes.index(actual.firstValue)
            for count_1 in range(len(matrix[index])):
                if matrix[index][count_1]:
                    newValue = nodes[count_1]
                else:
                    continue
                flag_2 = True
                flag_3 = False
                for count_2 in range(len(visited)):
                    if visited[count_2][0] == newValue:
                        if visited[count_2][1] == 2:
                            flag_2 = False
                        else:
                            flag_3 = True
                        break
                if flag_2:
                    myList_3.insertAtBack(actual, newValue, actual.secondValue + 1)
                    myList_4.insertAtBack(actual, newValue, actual.secondValue + 1)
                    if flag_3:
                        path = list()
                        path = myList_4.getTree()
                        path = path[::-1]
                        path += myList_2.getTree1(newValue)
                        return path
                    else:
                        line = list()
                        line.append(newValue)
                        line.append(2)
                        visited.append(line)

            if myList_3.isEmpty() != True:
                aux = myList_3.first()
                if aux.secondValue == actual.secondValue:
                    flag_1 = True
                else:
                    flag_1 = False

    return "Caminho não encontrado"
