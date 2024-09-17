from math import sqrt
from DoubleList import DoubleList
from math import sqrt
from DoubleList import DoubleList

class Chained_Hash:
    def __init__(self, m, metodo):
        self.m = int(m)  # Tamaño del arreglo
        self.metodo = metodo  # Método a utilizar
        self.arreglo = [None] * self.m  # Inicializar arreglo con None en todas las posiciones

    def insertar(self, valor):
        listaDoble = DoubleList()
        if self.metodo.lower() == "multiplicacion":
            indice = self.multiplicar(valor)
        elif self.metodo.lower() == "division":
            indice = self.dividir(valor)
        else:
            print("Elija un método válido: multiplicación o división")
            return
        
        # Si la posición está vacía, crea una lista doble y añade el elemento
        if self.arreglo[indice] is None:
            self.arreglo[indice] = listaDoble
            listaDoble.addLast(valor)
        else:
            # Si la posición ya está ocupada, añade el elemento a la lista doble existente
            self.arreglo[indice].addLast(valor)
        
        print(f"Elemento {valor} insertado en la posición {indice}")

    def buscar(self, valor):
        """Buscar un dato dada su clave."""
        if self.metodo.lower() == "multiplicacion":
            indice = self.multiplicar(valor)
        elif self.metodo.lower() == "division":
            indice = self.dividir(valor)
        else:
            print("Elija un método válido: multiplicación o división")
            return None
        
        listaDoble = self.arreglo[indice]
        
        if listaDoble is None:
            print(f"El valor {valor} no fue encontrado.")
            return None
        
        # Recorremos la lista doble en esa posición
        nodo = listaDoble.first()
        while nodo:
            if nodo.getData() == valor:
                print(f"Valor {valor} encontrado en la posición {indice}.")
                return valor
            nodo = nodo.next
        
        print(f"El valor {valor} no fue encontrado.")
        return None

    def eliminar(self, valor):
        """Eliminar un dato dada su clave."""
        if self.metodo.lower() == "multiplicacion":
            indice = self.multiplicar(valor)
        elif self.metodo.lower() == "division":
            indice = self.dividir(valor)
        else:
            print("Elija un método válido: multiplicación o división")
            return
        
        listaDoble = self.arreglo[indice]
        
        if listaDoble is None:
            print(f"El valor {valor} no se encuentra en la tabla.")
            return
        
        # Recorremos la lista doble en esa posición
        nodo = listaDoble.first()
        while nodo:
            if nodo.getData() == valor:
                listaDoble.remove(nodo)
                print(f"Valor {valor} eliminado de la posición {indice}.")
                return
            nodo = nodo.next
        
        print(f"El valor {valor} no se encuentra en la tabla.")
    
    def dividir(self, k):
        return k % self.m

    def multiplicar(self, k):
        a = (sqrt(5) - 1) / 2
        return int(self.m * ((k * a) % 1))  # Asegúrate de que sea un índice entero





    

