from BST import BST
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

