from Stack import Stack
pila = Stack()
#Añadiendo datos a la pila
pila.push(2)
pila.push(4)
pila.push(6)
pila.push(8)
pila.push(10)

while not pila.isEmpty():
    print(pila.pop())