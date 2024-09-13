import math

class Heap():
    def __init__(self, capacity, A=None):
        # Inicializa el heap con una capacidad máxima y un arreglo vacío o el arreglo A
        self.__capacity = capacity
        self.__A = A if A is not None else []  # Si se da un arreglo, lo uso; si no, uso una lista vacía
    
    # Método para obtener el arreglo interno del heap
    def getA(self):
        return self.__A

    # Calcula el índice del nodo padre de un nodo dado
    def parent(self, i):
        return math.ceil(i / 2) - 1

    # Calcula el índice del hijo izquierdo de un nodo dado
    def left(self, i):
        return (2 * i) + 1

    # Calcula el índice del hijo derecho de un nodo dado
    def right(self, i):
        return (2 * i) + 2

    # Mantiene la propiedad de max-heap en un nodo específico
    def max_heapify(self, i):
        heap_size = len(self.__A)
        l = self.left(i)
        r = self.right(i)
        if l < heap_size and self.__A[l] > self.__A[i]:
            largest = l
        else:
            largest = i
        if r < heap_size and self.__A[r] > self.__A[largest]:
            largest = r

        if largest != i:
            self.__A[i], self.__A[largest] = self.__A[largest], self.__A[i]
            self.max_heapify(largest)

    # Construye un max-heap a partir del arreglo ya existente en el heap
    def build_max_heap(self):
        for i in range((len(self.__A) // 2) - 1, -1, -1):
            self.max_heapify(i)

    # Ordena el arreglo usando heap sort
    def heap_sort(self):
        self.build_max_heap()
        heap_size = len(self.__A)
        for i in range(len(self.__A) - 1, 0, -1):
            self.__A[i], self.__A[0] = self.__A[0], self.__A[i]
            heap_size -= 1
            self.max_heapify(0)

    # Inserta un nuevo elemento en el heap y mantiene la propiedad de max-heap
    def max_heap_insert(self, k):
        self.__A.append(k)
        i = len(self.__A) - 1
        while i > 0 and self.__A[self.parent(i)] < self.__A[i]:
            self.__A[i], self.__A[self.parent(i)] = self.__A[self.parent(i)], self.__A[i]
            i = self.parent(i)

    # Extrae y devuelve el valor máximo del heap
    def heap_extract_max(self):
        heap_size = len(self.__A)
        if heap_size == 0:
            return None
        max_value = self.__A[0]
        self.__A[0] = self.__A[heap_size - 1]
        self.__A.pop()
        self.max_heapify(0)
        return max_value

    # Devuelve el valor máximo del heap (la raíz)
    def heap_maximum(self):
        return self.__A[0] if len(self.__A) > 0 else None






# Generar un arreglo de 20 enteros aleatorios entre 1 y 100
#arreglo_aleatorio = [random.randint(1, 100) for _ in range(20)]
arreglo = [1,20,15,30,50]

#print(arreglo_aleatorio)

#Probando las funcionalidades del Heap

#Construir un heap con la lista de núemeros aleatorios
heap = Heap(20,arreglo)

#Probando el max_heapify . Si le hago el max heapify al 21, me tiene que cambiar con el 86
print("Aplicando max_heapify al 21. Cambia la posición con el 86")
heap.max_heapify(9) #El 21 está en la posición i = 9
print(heap.getA()) # Revisando que se cumpla y el arreglo quede modificado


#Probando el build_max_heap
print("\nImprimiedno el heap después de aplicarle un buld_max_heap")
heap.build_max_heap()
print(heap.getA()) #Revisando que efectivamente hallan cambiado las posiciones del arreglo

#Probando el heap_sort
heap.heap_sort()
print(heap.getA())

#Probando el max_heap insert()
heap.max_heap_insert(2)
print("\nHeap después de agregarle un elemento con max_heap_insert")
print(heap.getA()) #Mostrando el arreglo con el nuevo elemeneto insertado

#Probando el heap_extract_max
heap2 = Heap(20,arreglo)
heap2.build_max_heap()
print(heap2.getA())
print(f"el máximo era {heap2.heap_extract_max()}. Ya quedó eliminado")
print(f"Ahora el máximo es {heap2.heap_maximum()}") #Probando el heap_maximum