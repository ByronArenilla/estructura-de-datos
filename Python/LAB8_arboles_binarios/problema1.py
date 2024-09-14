from BinarySearchTree import BinarySearchTree

# Crear el árbol de búsqueda binario
bst = BinarySearchTree()

# Insertar elementos
bst.insert("Valor 1", 10)
bst.insert("Valor 2", 5)
bst.insert("Valor 3", 15)
bst.insert("Valor 4", 2)
bst.insert("Valor 5", 7)
bst.insert("Valor 6", 12)
bst.insert("Valor 7", 20)

# Mostrar el árbol
print("Árbol binario de búsqueda:")
bst.printTree(bst.root())

# Recorrido inorder
print("\nRecorrido inorder:")
bst.inOrderTraversal(bst.root())
print()  # Nueva línea

# Encontrar máximo y mínimo
# Obtener el valor mínimo y máximo directamente
min_value = bst.findMin()  # Ya es un BSTEntry, no un Node
max_value = bst.findMax()  # Ya es un BSTEntry, no un Node


print(f"\nValor máximo: {max_value.getValue()} (Clave: {max_value.getKey()})")
print(f"Valor mínimo: {min_value.getValue()} (Clave: {min_value.getKey()})")

# Buscar un nodo
nodo = bst.find(7)
print(f"\nNodo encontrado: {nodo.getData().getValue()}")  # Debería imprimir "Valor 5"

# Eliminar un nodo
bst.remove(15)

# Mostrar el árbol después de eliminar
print("\nÁrbol binario después de eliminar el nodo con clave 15:")
bst.printTree(bst.root())
