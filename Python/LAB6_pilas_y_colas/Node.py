class Node():
    def __init__(self,data)  :
        self.__data = data
        self.__next = None
    
    #Método para establecer el dato de un nodo
    def setData(self, e):
        self.__data = e

    #Método para enlazar el nodo a uno siguiente
    def setNext(self, n):
            self.__next = n
    
    #Método para obtener el dato de un nodo
    def getData(self):
         return self.__data
    
    #Método para obtener el next de un nodo
    def getNext(self):
         return self.__next