from DTO.Node import Node

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