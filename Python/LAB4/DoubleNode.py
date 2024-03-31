
from Node import Node
class DoubleNode(Node):
    def __init__(self,data):
         super().__init__(data)
         self.__prev = None
    
    #Método para enlazar el nodo a uno anterior
    def setPrev(self, p):
         self.__prev = p

    #Método para obtener el prev de un nodo
    def getPrev(self):
         return self.__prev
# nodo = DoubleNode(10)
# print(nodo.getData())
# nodo.setNext(2)
# print(nodo.getNext())
# nodo.setPrev(15)
# print(nodo.getPrev())