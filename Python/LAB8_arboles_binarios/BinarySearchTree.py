from BinaryTree import BinaryTree
from Node import Node
from BSTEntry import BSTEntry 
# Clase BinarySearchTree que hereda de BinaryTree
class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    # Método find
    def find(self, k):
        return self.searchTree(k, self.root())

    def searchTree(self, key, v):
        if v is None:
            return None
        u = v.getData()
        if key == u.getKey():
            return v
        elif key < u.getKey():
            return self.searchTree(key, self.left(v))
        else:
            return self.searchTree(key, self.right(v))

    # Método insert
    def insert(self, value, key):
        new_entry = BSTEntry(value, key)
        if self.isEmpty():
            self.addRoot(new_entry)
        else:
            self.addEntry(self.root(), new_entry)

    def addEntry(self, v, new_entry):
        current_entry = v.getData()
        new_node = Node(new_entry)
        if new_entry.getKey() < current_entry.getKey():
            if self.hasLeft(v):
                self.addEntry(self.left(v), new_entry)
            else:
                v.setLeft(new_node)
                self._increaseSize()  # Usa el método para incrementar el tamaño
        else:
            if self.hasRight(v):
                self.addEntry(self.right(v), new_entry)
            else:
                v.setRight(new_node)
                self._increaseSize()  # Usa el método para incrementar el tamaño
    def findNode(self, key):
        current = self.root()  # Empezamos desde la raíz
        while current is not None:
            current_data = current.getData()  # Obtener el objeto BSTEntry
            if key == current_data.getKey():  # Si encontramos el nodo con la clave correcta
                return current  # Retornamos el nodo encontrado
            elif key < current_data.getKey():  # Si la clave es menor, buscamos en el subárbol izquierdo
                current = current.getLeft()
            else:  # Si la clave es mayor, buscamos en el subárbol derecho
                current = current.getRight()
        return None  # Si no encontramos el nodo, retornamos None
    
    def _removeNode(self, node):
        # Caso 1: El nodo no tiene hijos (es una hoja)
        if not self.hasLeft(node) and not self.hasRight(node):
            if self.isRoot(node):
                self._setRoot(None)  # Si es la raíz, eliminamos el árbol
            else:
                parent = self.parent(node)
                if self.left(parent) == node:
                    parent.setLeft(None)  # Desconectar de su padre
                else:
                    parent.setRight(None)
            self._decreaseSize()

        # Caso 2: El nodo tiene un solo hijo
        elif self.hasLeft(node) and not self.hasRight(node):  # Solo hijo izquierdo
            child = self.left(node)
            self._replaceNodeWithChild(node, child)
        elif not self.hasLeft(node) and self.hasRight(node):  # Solo hijo derecho
            child = self.right(node)
            self._replaceNodeWithChild(node, child)

        # Caso 3: El nodo tiene dos hijos
        else:
            # Encontrar el sucesor (mínimo del subárbol derecho)
            successor = self.findMin(self.right(node))
            # Copiar los valores del sucesor al nodo a eliminar
            node.getData().key = successor.getKey()
            node.getData().value = successor.getValue()
            # Eliminar el sucesor directamente, sin volver a buscar
            self._removeNode(successor)  # Eliminar el sucesor, que será una hoja o tendrá un solo hijo



    # Método remove (elimina un nodo con la clave k)
    def remove(self, key):
        node_to_remove = self.findNode(key)  # Debe retornar el nodo correspondiente a la clave
        if node_to_remove:
            self._removeNode(node_to_remove)
        else:
            print(f"El nodo con la clave {key} no existe.")

        # Caso 1: el nodo tiene dos hijos
        if self.hasLeft(v) and self.hasRight(v):
            successor = self._findMin(self.right(v))
            
            # Cambia los valores del nodo a eliminar por los del sucesor
            v.getData().value = successor.getValue()
            v.getData().key = successor.getKey()
            
            # Elimina el sucesor, que ahora está duplicado
            self._removeNode(successor)

        # Caso 2: el nodo tiene un solo hijo o ninguno
        else:
            child = v.getLeft() if self.hasLeft(v) else v.getRight()

            # Conectar al padre con el hijo
            if self.isRoot(v):
                self._setRoot(child)
            elif self.left(parent) == v:
                parent.setLeft(child)
            else:
                parent.setRight(child)

            v.setLeft(None)
            v.setRight(None)
            self._decreaseSize()

    def findMax(self):
        if self.isEmpty():
            return None
        current = self.root()
        while self.hasRight(current):
            current = self.right(current)
        return current.getData()


    def findMin(self, v=None):
        if v is None:
            v = self.root()  # Si no se pasa ningún nodo, usamos la raíz
        current = v
        while self.hasLeft(current):
            current = self.left(current)
        return current.getData()

    def _increaseSize(self):
        self._BinaryTree__size += 1

    def _decreaseSize(self):
        self._BinaryTree__size -= 1

    def isEmpty(self):
        return self._BinaryTree__size == 0
    
    def printTree(self, v, level=0):
        if v is not None:
            self.printTree(self.right(v), level + 1)
            print(' ' * 4 * level + '->', v.getData().getValue())
            self.printTree(self.left(v), level + 1)
    def inOrderTraversal(self, v):
        if v is not None:
            self.inOrderTraversal(self.left(v))
            print(v.getData().getKey(), end=' ')
            self.inOrderTraversal(self.right(v))