from BinarySearchTree import BinarySearchTree
from Usuario import Usuario
from mostrar_arbol import display_with_binarytree
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
print("Árbol Binario de Búsqueda:")
display_with_binarytree(bst)

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
display_with_binarytree(bst)

# Valor máximo y mínimo
print(f"\nUsuario con la clave máxima: {bst.find_max().data}")
print(f"Usuario con la clave mínima: {bst.find_min().data}")
