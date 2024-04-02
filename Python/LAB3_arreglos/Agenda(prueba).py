from Fecha import Fecha
from Direccion import Direccion
from Usuario import Usuario

#Nombre y ID
nombre = "Byron"
id = 1000192293
nombre2 = "Annie"
id2 = 1013338765


#Fecha


fecha = Fecha("23","03","2002")
fecha2 = Fecha("1","1","2005")

#Ciudad de nacimiento, tel y email
ciudad = "Medellin"
tel = 3148839303
email = "byronarenilla7@gmail.com"

ciudad2 = "Mede"
tel2 = 3224626761
email2 = "anniearenilla7@gmail.com"

#Dirección
direccion = Direccion("calle82a","90a-10","Robledo","Medellín")
direccion2 = Direccion("calle82a","90a-10","Robledo","Medellín")
# print(usuario.__str__())



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

    def toFile(self,filename = 'agenda_prueba.txt'):
        with open(filename, 'w') as file:
            for usuario in self._registro:
                file.write(f"{usuario}\n")

    def importar(self, filename='agenda_prueba.txt'):
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
                        self._no_reg += 1
                        
            print("Importación exitosa.")
        except FileNotFoundError:
            print(f"El archivo {filename} no existe.")
        except Exception as e:
            print(f"Error durante la importación: {e}")





#problemas si está en cero y si está en la última posición





usuario = Usuario(nombre,id,fecha,ciudad,tel,email,direccion)
usuario2 = Usuario(nombre2,id2,fecha2,ciudad2,tel2,email2,direccion2)

#Comprobando que el usuario sí se agrega, y no se vuelve a agregar si ya está.
agenda = Agenda(3)
print(agenda.agregar(usuario)[1])
# print(agenda.buscar(1000192293)) Comprobando que me devuelva la posicón de usuario
print(agenda.agregar(usuario)[1])
agenda.agregar(usuario2)

#Probando si borra corectamente
# print(agenda.eliminar(1002293)[1])
# print(agenda.eliminar(1013338765)[0])
# print(agenda.eliminar(1000192293)[1])


#Convirtiendo los datos de los usuarios en un archivo de texto.
agenda.toFile()

# Leer y mostrar el contenido del archivo
with open('agenda_prueba.txt', 'r') as file:
    content = file.read()
    print(content)

#Eliminando los datos y leyendo si hay algo
print(agenda.eliminar(1002293)[1])
print(agenda.eliminar(1013338765)[0])
print(agenda.eliminar(1000192293)[1])

#Mostrar cómo está el objeto en ese momento
print(agenda._no_reg)

#Importando los datos y agregandolos nuevamente como usuarios
agenda.importar()

# Leer y mostrar el contenido del archivo
with open('agenda_prueba.txt', 'r') as file:
    content = file.read()
    print(content)


#Mirar cómo está el objeto(Ver si realizó la importación correctamente)
print(agenda._no_reg)
print(agenda._registro)