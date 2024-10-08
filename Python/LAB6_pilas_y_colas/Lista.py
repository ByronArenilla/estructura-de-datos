from Node import Node 
class Lista():
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    

    #Método para retornar el tamaño de la lista
    def size(self):
        return self.__size
    
    #Método para decir si la lista está vacía
    def isEmpty(self):
        if self.__size == 0:
            return True
        else:
            return False
    
    #Método para establecer el tamaño de la lista
    def setSize(self,s):
        self.__size  = s
    
    #Métodos para establecer el primero de la lista y el último
    def first(self):
        return self.__head
    
    def last(self):
        return self.__tail
    
    #Métodos para añadir al primero y último de la lista 
    def addFirst(self, e):
        n = Node(e)
        if self.isEmpty():
            self.__head = n
            self.__tail = n
        else:
            n.setNext(self.__head)
            self.__head = n
        self.__size += 1

    def addLast(self, e):
        n = Node(e)
        if self.isEmpty():
            self.__head = n
            self.__tail = n
        else:
            self.__tail.setNext(n)
            self.__tail = n
        self.__size += 1
    #Métodos para elminar el primero y último de la lista 
    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            temp = self.__head
            self.__head = temp.getNext() #Estableciendo el head en la posición 2
            temp.setNext(None)
            self.__size -= 1
            return temp.getData()
    
    def removeLast(self):
        if self.__size == 1:
            return self.removeFirst()
        else:
            temp = self.__tail
            anterior = self.__head
            while anterior.getNext() != self.__tail:
                anterior = anterior.getNext()
        anterior.setNext(None)
        self.__tail = anterior 
        self.__size -= 1
        return temp.getData()
    
    def remove(self,n):
        temp = self.first()
        while (temp != None and temp.getData() != n ):
            anterior = temp
            temp = temp.getNext()
        if temp != None:
            anterior.setNext(temp.getNext())
            temp.setNext(None)
            self.setSize(self.size()-1)


        