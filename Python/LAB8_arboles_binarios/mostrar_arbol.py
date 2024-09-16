from binarytree import Node
def convert_to_binarytree(node):
    #Convierte un nodo de mi estructura a un nodo de binarytree
    if node is None:
        return None
    
    # Crear el nodo binarytree a partir de tu nodo
    new_node = Node(node.value.key)
    
    # Convertir el subárbol izquierdo y derecho
    new_node.left = convert_to_binarytree(node.left)
    new_node.right = convert_to_binarytree(node.right)
    
    return new_node

# Función para mostrar el árbol usando binarytree
def display_with_binarytree(bst):
    #Usa binarytree para mostrar el árbol binario de búsqueda
    root = convert_to_binarytree(bst.root)  # Convierte el árbol al formato de binarytree
    if root:
        print(root)  # Usa el print propio de binarytree para mostrar el árbol
    else:
        print("Árbol vacío")