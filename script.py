import numpy as np

def getData():
    matrix = np.array([
        [0,1,0,0,0,0],
        [1,0,1,0,1,0],
        [0,1,0,1,0,0],
        [0,0,1,0,0,1],
        [0,1,0,0,0,1],
        [0,0,0,1,1,0]
    ])
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']

    return matrix, nodes

def verifyMatrix(matrix, nodes):
    if matrix.shape[0] == matrix.shape[1]:
        if matrix.shape[0] == len(nodes):
            return True
        else:
            print("!!! ERROR !!!")
            print("> Os nós não são compatíveis com a matrix")
            return False
    else:
        print("!!! ERROR !!!")
        print("> A Matrix não é quadrada")
        return False

class Node(object):
    def __init__(self, father = None, firstValue = None, secondValue = None, previousNode = None, nextNode = None):
        """
        Script node

        :type father: Node
        :type firstValue: NoneType
        :type secondValue: NoneType
        :type previousNode: Node
        :type nextNode: Node
        """
        self.father = father
        self.firstValue = firstValue
        self.secondValue = secondValue
        self.previousNode = previousNode
        self.nextNode = nextNode

class MyList(object):
    __head: Node = None
    __tail: Node = None

    # INSERE NO INÍCIO DA LISTA
    def insertInFront(self, father: Node, firstValue, secondValue):
        newNode = Node(father, firstValue, secondValue, None, None)
        if self.__head == None:
            self.__tail = newNode
        else:
            newNode.nextNode = self.__head
            self.__head.previousNode = newNode
        self.__head = newNode

    # INSERE NO FIM DA LISTA
    def insertAtBack(self, father: Node, firstValue, secondValue):

        newNode = Node(father, firstValue, secondValue, None, None)

        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.nextNode = newNode
            newNode.previousNode = self.__tail
        self.__tail = newNode

    # REMOVE NO INÍCIO DA LISTA
    def deleteFirst(self):
        if self.__head is None:
            return None
        else:
            node = self.__head
            self.__head = self.__head.nextNode
            if self.__head is not None:
                self.__head.previousNode = None
            else:
                self.__tail = None
            return node

    # REMOVE NO FIM DA LISTA
    def deleteLast(self):
        if self.__tail is None:
            return None
        else:
            node = self.__tail
            self.__tail = self.__tail.previousNode
            if self.__tail is not None:
                self.__tail.nextNode = None
            else:
                self.__head = None
            return node

    def isEmpty(self):
        if self.__head is None:
            return True
        else:
            return False
        
    def getList(self):
        aux = self.__head
        myList = []
        while aux != None:
            myList.append(aux.firstValue)
            aux = aux.nextNode
        
        return myList
    
    def getTree(self):
        actual = self.__tail
        path = []
        while actual.father is not None:
            path.append(actual.firstValue)
            actual = actual.father
        path.append(actual.firstValue)
        return path
    
    def getTree1(self, value):
        actual = self.__head
        while actual.firstValue != value:
            actual = actual.nextNode
    
        caminho = []
        actual = actual.father
        while actual.father is not None:
            caminho.append(actual.firstValue)
            actual = actual.father
        caminho.append(actual.firstValue)
        return caminho
    
    
    def first(self) -> Node:
        return self.__head
    
    def last(self) -> Node:
        return self.__tail

class Search(object):
    def __init__(self, matrix: np.ndarray, nodes: list):
        self.matrix = matrix
        self.nodes = nodes

    def amplitude(self, start, end):
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
            index = self.nodes.index(actual.firstValue)
            for count_1 in range(len(self.matrix[index])):
                if self.matrix[index][count_1]:
                    newValue = self.nodes[count_1]
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

if __name__ == '__main__':
    matrix, nodes = getData()
    print("> Dados capturados, matrix pronta")
    if not verifyMatrix(matrix, nodes):
        exit(0)
    print("> Matrix validada com sucesso")

    search = Search(matrix, nodes)

    print("> Iniciando busca em amplitude")
    path = search.amplitude('A', 'D')
    newPath = []
    for item in reversed(path):
        newPath.append(item)
    print(newPath)
