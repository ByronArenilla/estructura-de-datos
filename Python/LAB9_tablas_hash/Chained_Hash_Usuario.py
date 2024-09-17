from math import sqrt
from DoubleList import DoubleList
from math import sqrt
from DoubleList import DoubleList

class Chained_Hash_Usuario:
    def __init__(self, m, metodo):
        self.m = int(m)  # Tamaño del arreglo
        self.metodo = metodo  # Método a utilizar
        self.arreglo = [None] * self.m  # Inicializar arreglo con None en todas las posiciones

    def insertar(self, usuario):
        listaDoble = DoubleList()
        id_usuario = int(usuario.getId())
        
        if self.metodo.lower() == "multiplicacion":
            indice = self.multiplicar(id_usuario)
        elif self.metodo.lower() == "division":
            indice = self.dividir(id_usuario)
        else:
            print("Elija un método válido: multiplicación o división")
            return
        
        # Si la posición está vacía, crea una lista doble y añade el elemento
        if self.arreglo[indice] is None:
            self.arreglo[indice] = listaDoble
            listaDoble.addLast(usuario)
        else:
            # Si la posición ya está ocupada, añade el elemento a la lista doble existente
            self.arreglo[indice].addLast(usuario)

        print(f"El usuario {usuario.getNombre()} con número de identificación {usuario.getId()} ha sido insertado en la posición {indice}")

    def buscar(self, id_usuario):
        # Determinar el índice usando el método seleccionado (multiplicación o división)
        if self.metodo.lower() == "multiplicacion":
            indice = self.multiplicar(id_usuario)
        elif self.metodo.lower() == "division":
            indice = self.dividir(id_usuario)
        else:
            print("Elija un método válido: multiplicación o división")
            return None

        # Obtener la lista doble en esa posición del arreglo
        listaDoble = self.arreglo[indice]

        if listaDoble is None:
            print(f"El usuario con ID {id_usuario} no fue encontrado en la tabla.")
            return None

        # Recorremos la lista doble en esa posición
        nodo = listaDoble.first()
        while nodo:
            usuario = nodo.getData()
            if usuario.getId() == id_usuario:
                print(f"Usuario {usuario.getNombre()} con númerod de identificación  {id_usuario}) encontrado en la posición {indice}.")
                return usuario  # Retornamos el usuario si lo encontramos
            nodo = nodo.getNext()

    def eliminar(self, id_usuario):
        # Determinar el índice usando el método seleccionado (multiplicación o división)
        if self.metodo.lower() == "multiplicacion":
            indice = self.multiplicar(id_usuario)
        elif self.metodo.lower() == "division":
            indice = self.dividir(id_usuario)
        else:
            print("Elija un método válido: multiplicación o división")
            return
        
        # Obtener la lista doble en esa posición del arreglo
        listaDoble = self.arreglo[indice]

        if listaDoble is None:
            print(f"El usuario con ID {id_usuario} no se encuentra en la tabla.")
            return
        
        # Recorremos la lista doble en esa posición
        nodo = listaDoble.first()
        while nodo:
            usuario = nodo.getData()
            if usuario.getId() == id_usuario:
                # Eliminamos el nodo de la lista doble
                listaDoble.remove(nodo)
                print(f"Usuario {usuario.getNombre()} con número de identificación {id_usuario}) eliminado de la posición {indice}.")
                return
            nodo = nodo.getNext()

        # Si no encontramos el usuario en la lista doble
        print(f"El usuario con ID {id_usuario} no se encuentra en la tabla.")

    
    def dividir(self, k):
        return k % self.m

    def multiplicar(self, k):
        a = (sqrt(5) - 1) / 2
        return int(self.m * ((k * a) % 1))  # Asegúrate de que sea un índice entero


