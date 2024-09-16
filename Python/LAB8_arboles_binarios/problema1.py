from BinarySearchTree import BinarySearchTree
from binarytree import Node
from mostrar_arbol import display_with_binarytree



# Crear una instancia de BinarySearchTree
bst = BinarySearchTree()

# Insertar varios nodos en el árbol
print("Insertando nodos...")
bst.insert(50, "Dato 50")
bst.insert(30, "Dato 30")
bst.insert(20, "Dato 20")
bst.insert(40, "Dato 40")
bst.insert(70, "Dato 70")
bst.insert(60, "Dato 60")
bst.insert(80, "Dato 80")

# Mostrar el árbol
display_with_binarytree(bst)

# Buscar un nodo
print("\nBuscando nodo con clave 40:")
nodo_buscado = bst.search(40)
if nodo_buscado:
    print(f"Encontrado: {nodo_buscado.value}")
else:
    print("No encontrado.")

# Eliminar un nodo
print("\nEliminando nodo con clave 30:")
bst.delete(30)


# Mostrar el árbol después de eliminar un nodo
display_with_binarytree(bst)

# Buscar el valor máximo
print("\nValor máximo en el árbol:")
max_value = bst.find_max()
print(f"Máximo: {max_value}")

# Buscar el valor mínimo
print("\nValor mínimo en el árbol:")
min_value = bst.find_min()
print(f"Mínimo: {min_value}")

# Realizar un recorrido inorder
print("\nRecorrido inorder del árbol:")
bst.inorder()
