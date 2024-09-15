from binarytree import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserta un nuevo nodo en el BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        """Elimina un nodo dado su clave, manteniendo las propiedades del BST."""
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, node, key):
        if node is None:
            return node
        
        if key < node.value:
            node.left = self._delete_node(node.left, key)
        elif key > node.value:
            node.right = self._delete_node(node.right, key)
        else:
            # Caso 1: Nodo hoja
            if node.left is None and node.right is None:
                return None
            # Caso 2: Un solo hijo
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Caso 3: Dos hijos
            else:
                min_node = self._find_min(node.right)
                node.value = min_node.value
                node.right = self._delete_node(node.right, min_node.value)
        return node

    def search(self, key):
        """Busca un nodo por su clave."""
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def find_max(self):
        """Encuentra el valor máximo en el BST."""
        if self.root is None:
            return None
        return self._find_max(self.root).value

    def _find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def find_min(self):
        """Encuentra el valor mínimo en el BST."""
        if self.root is None:
            return None
        return self._find_min(self.root).value

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def display(self):
        """Muestra el árbol binario."""
        print(self.root)

    def inorder(self):
        """Muestra el recorrido inorder del BST."""
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.value, end=' ')
            self._inorder(node.right)
if __name__ == "__main__":
    bst = BST()
    
    # Insertar nodos
    keys = [50, 30, 20, 40, 70, 60, 80]
    for key in keys:
        bst.insert(key)

    print("Árbol BST:")
    bst.display()

    print("\nRecorrido Inorder:")
    bst.inorder()

    # Buscar un nodo
    key_to_search = 40
    found_node = bst.search(key_to_search)
    print(f"\nNodo encontrado: {found_node}")

    # Eliminar un nodo
    key_to_delete = 70
    bst.delete(key_to_delete)
    print(f"\nÁrbol después de eliminar {key_to_delete}:")
    bst.display()

    # Valor máximo y mínimo
    print(f"\nValor máximo: {bst.find_max()}")
    print(f"Valor mínimo: {bst.find_min()}")

