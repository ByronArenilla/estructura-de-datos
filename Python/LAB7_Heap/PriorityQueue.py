from Heap import Heap
class PriorityQueue(Heap):
    def __init__(self, capacity, A = None):
        super().__init__(capacity, A)

edades_clientes = [10,25,30,45,14,78,26,23]
priorityQueue = PriorityQueue(10)
print(priorityQueue.getA())

#Voy ingresando los clientes que lleguen
for i in range(len(edades_clientes)):
    priorityQueue.max_heap_insert(edades_clientes[i])
    #print(priorityQueue.getA())
print(priorityQueue.getA())

for i in range(len(edades_clientes)):
    cliente_atendido = priorityQueue.heap_extract_max()
    siguiente_cliente = priorityQueue.heap_maximum()

    if siguiente_cliente is not None:
        print(f'El cliente con {cliente_atendido} años ya fue atendido. Ahora será atendido el cliente con {siguiente_cliente} años.')
    else:
        print(f'El cliente con {cliente_atendido} años ya fue atendido. No quedan más clientes en la cola.')
