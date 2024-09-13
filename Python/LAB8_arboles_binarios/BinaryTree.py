from Queue import Queue
from Node import Node
class BinaryTree():
    def __init__(self) :
        self.__root = None
        self.__size = 0

    #Tamaños del árbol
    def size(self):
        return self.__size
    def isEmpty(self):
        return self.__size == 0
    
    #Métodos booleanos
    def isRoot(self, v):
        return v == self.__root
    
    def hasLeft(self,v):
        return v.getLeft() != None
    
    def hasRight(self, v):
        return v.getRight() != None
    
    def isInternal(self, v):
        return self.hasLeft(v) or self.hasRight(v)
    
    #Métodos de altura y profundidad
    def depth(self, v):
        if self.isRoot(v): #Caso base
            return 0
        else: #Llamado recursivo
            return 1 + self.depth(self.parent(v))
    
    def height(self, v):
        if not self.isInternal(self,v): #Caso base
            return 0
        else:
            h = 0
            h = max(self.height(self.left))
            return 1 + h
    
    #Métodos acceso a nodos
    def root(self):
        return self.__root
    
    def left(self, v):
        return v.getLeft()
    
    def right(self,v):
        return v.getRight()
    
    def parent(self,v):
        if self.isRoot(v):
            return None
        
        else:
            Q = Queue()
            Q.enqueque(self.__root)
            temp = self.__root
        while not Q.isEmpty() and self.left(Q.first()) != v and self.right(Q.first()) != v:
            temp = Q.dequeque()

        if self.hasLeft(temp):
            Q.enqueque(self.left(temp))
        if self.hasRight(temp):
            Q.enqueque(self.right(temp))
        return temp
    
    def addRoot(self, e):
        self.__root = Node(e) 
        self.__size= 1

    
    def insertLeft(self, v,e):
        left = Node(e)
        v.setLeft(self.left())
        self.__size +=1
    
    def insertRight(self, v, e):
        right = Node(e)
        v.setRight(self.right())
        self.__size += 1

    def remove(self,v):
        p = self.parent(v)
        #v tiene al menos un hijo - caso 1
        if self.hasLeft(v) or self.hasRight(v):
            if self.hasLeft(v):
                child = self.left(v)
            else:
                child = self.right(v)
            #Se conceta el hijo de v al padre
            if self.left(p) == v:
                p.setLeft(child)
            else:
                p.setRigth(child)

            #Se desconecta el nodo v
            v.setLeft(None)
            v.setNext(None)
        else:
            # v no tiene hijos - caso 2
            if self.left(p) == v:
                p.setLeft(None)
            else:
                p.setRigth(None)





