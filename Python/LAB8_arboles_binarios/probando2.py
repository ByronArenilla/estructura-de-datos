from BinarySearchTree import BinarySearchTree

# Crear un árbol de búsqueda binario
bst = BinarySearchTree()

# Insertar elementos
bst.insert("Valor 1", 10)
bst.insert("Valor 2", 5)
bst.insert("Valor 3", 15)
bst.insert("Valor 4", 2)
bst.insert("Valor 5", 7)
bst.insert("Valor 6", 12)
bst.insert("Valor 7", 20)

# Buscar un nodo
nodo = bst.find(7)
print(f"Nodo encontrado: {nodo.getData().getValue()}")  # Debería imprimir "Valor 5"

# Eliminar un nodo
bst.remove(15)

