#Esto es un nodo dobel, sólo que en vez de prev y next tiene left y rigth
class Node():
     def __init__(self,data):
         self.__data = data
         self.left = None
         self.rigth = None

         ##Set

     #Método para establecer el dato de un Nodo
     def setData(self,d):
         self.__data = d
     
     #Método para establecer la conexión al nodo siguiente
     def setRigth(self,n):
         self.rigth = n
     
     #Método para establecer la conexión al nodo izquierdo
     def setLeft(self,p):
         self.left = p

         ##Get
     
     def getData(self):
         return self.__data
     
     def getRigth(self):
         return self.rigth
     
     def getLeft(self):
         return self.left
