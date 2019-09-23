import numpy as np
from DTO.MyList import MyList

def amplitude(matrix: np.ndarray, nodes: list, start, end):
    myList_1 = MyList()
    myList_2 = MyList()
    visited = list()

    myList_1.insertAtBack(None, start, 0)
    myList_2.insertAtBack(None, start, 0)
    line = list()
    line.append(start)
    line.append(0)
    visited.append(line)

    flag_1 = False
    while myList_1.isEmpty() is not True and flag_1 == False:
        actual = myList_1.deleteFirst()
        index = nodes.index(actual.firstValue)
        for count_1 in range(len(matrix[index])):
            if matrix[index][count_1]:
                newValue = nodes[count_1]
            else:
                continue
            flag = True
            for count_2 in range(len(visited)):
                if visited[count_2][0] == newValue:
                    flag = False
                    break
            if flag:
                myList_1.insertAtBack(actual, newValue, actual.secondValue + 1)
                myList_2.insertAtBack(actual, newValue, actual.secondValue + 1)
                line = list()
                line.append(newValue)
                line.append(actual.secondValue + 1)
                visited.append(line)
                if newValue == end:
                    flag_1 = True
                    break
    
    path = []
    if flag_1:
        path = myList_2.getTree()
    else:
        path = "Caminho não encontrado"
    
    return path