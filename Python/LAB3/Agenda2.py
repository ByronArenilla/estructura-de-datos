from Fecha import Fecha
from Direccion import Direccion
from Usuario import Usuario

class Agenda:
    def __init__(self, limite):
        self._registro = []  # Inicializa el registro como una lista vacía
        self._no_reg = 0
        self._limite = limite

    def agregar(self,u):
        if self.buscar(u.getId()) == -1: #-1 significa que no lo encuentra
            while self._no_reg < self._limite:
                self._registro.append(u)
                self._no_reg +=1
                mensaje = "Usuario agregado con éxito"
                return True, mensaje
        mensaje = "No fue posible agregar el usuario"
        return False, mensaje

    def buscar(self, id):
        for i in range(len(self._registro)):  # Corrige la iteración sobre la longitud de la lista
            if  self._registro[i].getId() == id:
                return i
        return -1

    def eliminar(self, id):
        if self.buscar(id) == -1:
            return False, "El ususario no existe, no es posible eliminarlo"
        else :
            temp = self._registro[self.buscar(id)]
            for i in range  (self.buscar(id),self._no_reg-1):
                    self._registro[i] = self._registro[i+1]
            self._registro[self._no_reg-1] = None
            self._no_reg -= 1

            # Eliminar elementos None del registro
            self._registro = [usuario for usuario in self._registro if usuario is not None]
            return temp, "El usuario ha sido eliminado"

    def toFile(self,filename = 'agenda2.txt'):
        with open(filename, 'w') as file:
            for usuario in self._registro:
                file.write(f"{usuario}\n")

    def importar(self, filename='agenda.txt'):
        try:
            with open(filename, 'r') as file:
                # Leer cada línea del archivo
                agenda = file.readlines()

                # Procesar cada línea y agregar usuarios al registro
                for linea in agenda:
                    usuario = linea.strip().split('/')
                    # Aquí puedes personalizar cómo interpretas los datos según tu estructura
                    if len(usuario) == 7:
                        nombre, id, fecha_nacimiento,ciudad_nacimiento,tel,email,dir = usuario
                        usuario = Usuario(nombre,id,fecha_nacimiento,ciudad_nacimiento,tel,email,dir)
                        self._registro.append(usuario)
            print("Importación exitosa.")
            self._no_reg +=1
        except FileNotFoundError:
            print(f"El archivo {filename} no existe.")
        except Exception as e:
            print(f"Error durante la importación: {e}")


#Definiendo la capacidad de la agenda
agenda = Agenda(5)

#Agregando usuarios con importar
agenda.importar()

#Imprimiendo en pantallas los resultados
for i in range(5):
    print(agenda._registro[i])

#Eliminando el usuario dado el ID
print(agenda.eliminar("1000192293"))

#Almacenar lista de usuarios actualizados
agenda.toFile()


