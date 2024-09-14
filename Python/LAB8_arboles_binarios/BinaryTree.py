from Queue import Queue
from Node import Node

class BinaryTree():
    def __init__(self):
        self.__root = None
        self.__size = 0

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    # Métodos booleanos
    def isRoot(self, v):
        return v == self.__root
    
    def hasLeft(self, v):
        return v.getLeft() is not None
    
    def hasRight(self, v):
        return v.getRight() is not None
    
    def isInternal(self, v):
        return self.hasLeft(v) or self.hasRight(v)
    
    # Métodos de altura y profundidad
    def depth(self, v):
        if self.isRoot(v):  # Caso base
            return 0
        else:  # Llamada recursiva
            return 1 + self.depth(self.parent(v))
    
    def height(self, v):
        if not self.isInternal(v):  # Caso base
            return 0
        else:
            h = 0
            if self.hasLeft(v):
                h = max(h, self.height(self.left(v)))
            if self.hasRight(v):
                h = max(h, self.height(self.right(v)))
            return 1 + h
    
    # Métodos de acceso a nodos
    def root(self):
        return self.__root
    
    def left(self, v):
        return v.getLeft()
    
    def right(self, v):
        return v.getRight()
    
    def parent(self, v):
        if self.isRoot(v):
            return None
        else:
            Q = Queue()
            Q.enqueque(self.__root)  # Cambiado a enqueque en lugar de put
            temp = self.__root
        
        while not Q.isEmpty() and self.left(temp) != v and self.right(temp) != v:
            temp = Q.dequeque()

            if self.hasLeft(temp):
                Q.enqueque(self.left(temp))
            if self.hasRight(temp):
                Q.enqueque(self.right(temp))
        return temp
    
    # Métodos de inserción
    def addRoot(self, e):
        self.__root = Node(e)
        self.__size = 1
    
    def insertLeft(self, v, e):
        left = Node(e)
        v.setLeft(left)
        self.__size += 1
    
    def insertRight(self, v, e):
        right = Node(e)
        v.setRight(right)
        self.__size += 1

    # Método para eliminar un nodo
    def remove(self, v):
        p = self.parent(v)
        
        # Caso 1: el nodo tiene un hijo
        if self.hasLeft(v) or self.hasRight(v):
            child = self.left(v) if self.hasLeft(v) else self.right(v)
            
            if self.left(p) == v:
                p.setLeft(child)
            else:
                p.setRight(child)

            v.setLeft(None)
            v.setRight(None)
        
        # Caso 2: el nodo no tiene hijos
        else:
            if self.left(p) == v:
                p.setLeft(None)
            else:
                p.setRight(None)
        self.__size -= 1

    def size(self):
        return self.__size
