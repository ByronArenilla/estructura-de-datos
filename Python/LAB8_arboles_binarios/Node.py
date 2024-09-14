class Node:
    def __init__(self, data):
        self.__data = data
        self.left = None
        self.right = None
        self.__next = None  # Añadir atributo __next para listas enlazadas

    ## Setters para el árbol binario
    def setData(self, d):
        self.__data = d

    def setRight(self, n):
        self.right = n

    def setLeft(self, p):
        self.left = p

    ## Setters y Getters para listas enlazadas
    def setNext(self, n):  # Método para listas enlazadas
        self.__next = n

    def getNext(self):  # Método para listas enlazadas
        return self.__next

    ## Getters para el árbol binario
    def getData(self):
        return self.__data

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left