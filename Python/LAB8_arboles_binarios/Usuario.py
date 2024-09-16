class BSTEntry:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __str__(self):
        return f"Clave: {self.key}, Datos: {self.data}"
class BinaryTree:
    def __init__(self, value):
        self.value = value  # Valor es un objeto de tipo BSTEntry
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        """Inserta un nuevo dato en el BST."""
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
        """Elimina un nodo dado su clave."""
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
        """Busca un nodo por su clave."""
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.value.key == key:
            return node
        if key < node.value.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def find_max(self):
        """Encuentra el valor máximo en el BST."""
        if self.root is None:
            return None
        return self._find_max(self.root).value

    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def find_min(self):
        """Encuentra el valor mínimo en el BST."""
        if self.root is None:
            return None
        return self._find_min(self.root).value

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def display(self):
        """Muestra el árbol binario."""
        self._display(self.root, 0)

    def _display(self, node, level):
        if node is not None:
            self._display(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self._display(node.left, level + 1)

    def inorder(self):
        """Realiza un recorrido inorder del BST."""
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.value, end=' ')
            self._inorder(node.right)

class Usuario:
    def __init__(self, nombre, id_numero):
        self.nombre = nombre
        self.id_numero = id_numero
        self.clave = self._sumar_digitos(id_numero)

    def _sumar_digitos(self, numero):
        return sum(int(digito) for digito in str(numero))

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_numero}, Clave: {self.clave}"
if __name__ == "__main__":
    # Crear árbol binario de búsqueda
    bst = BinarySearchTree()

    # Crear usuarios
    usuarios = [
        Usuario("Juan", 10101013),
        Usuario("Pablo", 10001011),
        Usuario("Maria", 10101015),
        Usuario("Ana", 1010000),
        Usuario("Diana", 10111105),
        Usuario("Mateo", 10110005)
    ]

    # Insertar usuarios en el árbol binario de búsqueda
    for usuario in usuarios:
        bst.insert(usuario.clave, usuario)

    # Mostrar el árbol
    print("Árbol Binario de Búsqueda (ABB):")
    bst.display()

    # Realizar recorrido inorder
    print("\nRecorrido Inorder del ABB:")
    bst.inorder()

    # Buscar un nodo
    clave_buscar = 7  # Clave de Juan
    nodo_encontrado = bst.search(clave_buscar)
    print(f"\nNodo encontrado con clave {clave_buscar}: {nodo_encontrado.value.data if nodo_encontrado else 'No encontrado'}")

    # Eliminar un nodo
    clave_eliminar = 10  # Clave de Diana
    bst.delete(clave_eliminar)
    print(f"\nÁrbol después de eliminar la clave {clave_eliminar}:")
    bst.display()

    # Valor máximo y mínimo
    print(f"\nUsuario con la clave máxima: {bst.find_max().data}")
    print(f"Usuario con la clave mínima: {bst.find_min().data}")
