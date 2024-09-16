from BSTEntry import BSTEntry
from BinaryTree import BinaryTree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        #Insertar un nuevo dato en el BST
        new_entry = BSTEntry(key, data)
        if self.root is None:
            self.root = BinaryTree(new_entry)
        else:
            self._insert(self.root, new_entry)

    def _insert(self, node, new_entry):
        if new_entry.key < node.value.key:
            if node.left is None:
                node.left = BinaryTree(new_entry)
            else:
                self._insert(node.left, new_entry)
        else:
            if node.right is None:
                node.right = BinaryTree(new_entry)
            else:
                self._insert(node.right, new_entry)

    def delete(self, key):
        #Eliminar un nodo dado su clave
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.value.key:
            node.left = self._delete(node.left, key)
        elif key > node.value.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.value.key)
        return node

    def search(self, key):
        #Buscar un nodo por su clave
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.value.key == key:
            return node
        if key < node.value.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def find_max(self):
        #Encontrar el valor máximo en el BST
        if self.root is None:
            return None
        return self._find_max(self.root).value

    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def find_min(self):
        #Encontrar el valor mínimo en el BST
        if self.root is None:
            return None
        return self._find_min(self.root).value

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder(self):
        #Realiza un recorrido inorder del BST
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.value, end=' ')
            self._inorder(node.right)
