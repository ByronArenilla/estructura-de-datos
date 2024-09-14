from Node import Node
from BinaryTree import BinaryTree


# Crear un árbol binario
tree = BinaryTree()

# Añadir la raíz
tree.addRoot(10)
root = tree.root()

# Insertar nodos a la izquierda y derecha de la raíz
tree.insertLeft(root, 5)
tree.insertRight(root, 15)

# Insertar nodos adicionales para probar más métodos
left_child = tree.left(root)
right_child = tree.right(root)

tree.insertLeft(left_child, 2)
tree.insertRight(left_child, 7)
tree.insertLeft(right_child, 12)
tree.insertRight(right_child, 20)

# Prueba de si los nodos tienen hijos
print(f"¿La raíz tiene hijo izquierdo?: {tree.hasLeft(root)}")  # True
print(f"¿La raíz tiene hijo derecho?: {tree.hasRight(root)}")  # True

# Probar si un nodo es interno (tiene al menos un hijo)
print(f"¿El nodo con valor 5 es interno?: {tree.isInternal(left_child)}")  # True
print(f"¿El nodo con valor 2 es interno?: {tree.isInternal(tree.left(left_child))}")  # False

# Probar profundidad de nodos
print(f"Profundidad de la raíz: {tree.depth(root)}")  # 0
print(f"Profundidad del nodo con valor 5: {tree.depth(left_child)}")  # 1
print(f"Profundidad del nodo con valor 2: {tree.depth(tree.left(left_child))}")  # 2

# Probar altura del árbol
print(f"Altura del árbol desde la raíz: {tree.height(root)}")  # 2
print(f"Altura del nodo con valor 5: {tree.height(left_child)}")  # 1

# Probar obtener el padre de un nodo
print(f"Padre del nodo con valor 5: {tree.parent(left_child).getData()}")  # 10
print(f"Padre del nodo con valor 12: {tree.parent(tree.left(right_child)).getData()}")  # 15

# Probar eliminar un nodo sin hijos
print(f"Tamaño antes de eliminar nodo con valor 2: {tree.size()}")  # 7
tree.remove(tree.left(left_child))  # Eliminar nodo con valor 2
print(f"Tamaño después de eliminar nodo con valor 2: {tree.size()}")  # 6

# Verificar si el nodo fue eliminado
print(f"¿El nodo con valor 5 tiene hijo izquierdo?: {tree.hasLeft(left_child)}")  # False

# Probar eliminar un nodo con un hijo
print(f"Tamaño antes de eliminar nodo con valor 7: {tree.size()}")  # 6
tree.remove(tree.right(left_child))  # Eliminar nodo con valor 7
print(f"Tamaño después de eliminar nodo con valor 7: {tree.size()}")  # 5
print(f"¿El nodo con valor 5 tiene hijo derecho?: {tree.hasRight(left_child)}")  # False
