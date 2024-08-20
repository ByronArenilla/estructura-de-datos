from Queque import Queque
queque = Queque()
#Agregando valores a la cola
queque.enqueque(2)
queque.enqueque(4)
queque.enqueque(6)
queque.enqueque(8)
queque.enqueque(10)

#Imprimir método dequeque
while not queque.isEmpty():
    print(queque.dequeque())