class DoubleNode():
     def __init__(self,data):
         self.__data = data
         self.__prev = None
         self.__next = None

         ##Set

     #Método para establecer el dato de un Nodo
     def setData(self,d):
         self.__data = d
     
     #Método para establecer la conexión al nodo siguiente
     def setNext(self,n):
         self.__next = n
     
     #Método para establecer la conexión al nodo previo
     def setPrev(self,p):
         self.__prev = p

         ##Get
     
     def getData(self):
         return self.__data
     
     def getNext(self):
         return self.__next
     
     def getPrev(self):
         return self.__prev

 ##Pruebas             
# nodo = DoubleNode(10)
# print(nodo.getData())
# nodo.setNext(2)
# print(nodo.getNext())
# nodo.setPrev(15)
# print(nodo.getPrev())