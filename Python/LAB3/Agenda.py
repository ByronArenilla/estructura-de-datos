from Fecha import Fecha
from Direccion import Direccion
from Usuario import Usuario

##Creando los 5 Usuarios
#Nombre y ID
nombre = "Byron"
id = "1000192293"
nombre2 = "Annie"
id2 = "1013338765"
nombre3= "Obelis"
id3 = "32007474"
nombre4= "Eduardo"
id4= "71180392"
nombre5 = "Daniela"
id5 = "1152717379"


#Fecha
fecha = Fecha("23","03","2002")
fecha2 = Fecha("1","4","2005")
fecha3 = Fecha ("11","12","1978")
fecha4 = Fecha("22","12","1978")
fecha5 = Fecha("7","10","1999")

#Ciudad de nacimiento, tel y email
ciudad = "Medellin"
tel = 3148839303
email = "byronarenilla7@gmail.com"

ciudad2 = "Medellin"
tel2 = 3224626761
email2 = "anniearenilla7@gmail.com"

ciudad3 = "San Pablo"
tel3 = 3224636377
email3 = "obelisramirez11@gmail.com"

ciudad4 = "Medellin"
tel4 = 3207074917
email4 = "edarenilla@gmail.com"

ciudad5 = "El bagre"
tel5 = 3223955828
email5 = "danicb.dc@gmail.com"






#Dirección
direccion = Direccion("calle82a","90a-10","Robledo","Medellin")
direccion2 = Direccion("calle82a","90a-10","Robledo","Medellin")
direccion3 = Direccion("calle82a","90a-10","Robledo","Medellin")
direccion4 = Direccion("calle83","89-36","Robledo","Medellin")
direccion5 = Direccion("calle70","70-21","Robledo", "Medellin")




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
        for i in range(len(self._registro)):  
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

    def toFile(self,filename = 'agenda.txt'):
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
                        self._no_reg +=1
            print("Importación exitosa.")
        except FileNotFoundError:
            print(f"El archivo {filename} no existe.")
        except Exception as e:
            print(f"Error durante la importación: {e}")


#creando los usuarios
usuario1 = Usuario(nombre,id,fecha,ciudad,tel,email,direccion)
usuario2 = Usuario(nombre2,id2,fecha2,ciudad2,tel2,email2,direccion2)
usuario3 = Usuario(nombre3,id3,fecha3,ciudad3,tel3,email3,direccion3)
usuario4 = Usuario(nombre4,id4,fecha4,ciudad4,tel4,email4,direccion4)
usuario5 = Usuario(nombre5,id5,fecha5,ciudad5,tel5,email5,direccion5)

#Agregando los usuarios a la agenda
agenda = Agenda(5) #límite de usuarios que se puede agregar
agenda.agregar(usuario1)
agenda.agregar(usuario2)
agenda.agregar(usuario3)
agenda.agregar(usuario4)
agenda.agregar(usuario5)

#Buscando un usuario
print(f"El usuario se encuentra almacenado en la posición {agenda.buscar('1000192293')} ")

#Almacenando todos los usuarios de la Agenda
agenda.toFile()

