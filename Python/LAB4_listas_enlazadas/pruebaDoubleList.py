from DoubleList import DoubleList

listaDoble = DoubleList()
for i in range (2,21,2):
    DoubleList.addLast(i)
print(DoubleList.first().getData())
print(DoubleList.last().getData())
pass

# Mostrando cada elemento de la lista
print("Elementos de la lista")
current_node = lista.first()
while current_node is not None:
    print(current_node.getData())
    current_node = current_node.getNext()

#Eliminando el 10 y el 12
lista.remove(10)
lista.removeLast()

#Mostrando nuevamente la lista
print("\nElementos de la lista modificada")
current_node = lista.first()
while current_node is not None:
    print(current_node.getData())
    current_node = current_node.getNext()