from DoubleList import DoubleList

listaDoble = DoubleList()
for i in range (2,21,2):
    listaDoble.addLast(i)
print(listaDoble.first().getData())
print(listaDoble.last().getData())

# Mostrando cada elemento de la lista
print("Elementos de la lista")
current_node = listaDoble.first()
while current_node is not None:
    print(current_node.getData())
    current_node = current_node.getNext()

#Eliminando el 10 y el 12
listaDoble.remove(10)
listaDoble.removeLast()

#Mostrando nuevamente la lista
print("\nElementos de la lista modificada")
current_node = listaDoble.first()
while current_node is not None:
    print(current_node.getData())
    current_node = current_node.getNext()