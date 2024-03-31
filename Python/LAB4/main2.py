from Fecha import Fecha
from Direccion import Direccion
from Usuario import Usuario
from DoubleList import DoubleList

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



#creando los usuarios
usuario1 = Usuario(nombre,id,fecha,ciudad,tel,email,direccion)
usuario2 = Usuario(nombre2,id2,fecha2,ciudad2,tel2,email2,direccion2)
usuario3 = Usuario(nombre3,id3,fecha3,ciudad3,tel3,email3,direccion3)
usuario4 = Usuario(nombre4,id4,fecha4,ciudad4,tel4,email4,direccion4)
usuario5 = Usuario(nombre5,id5,fecha5,ciudad5,tel5,email5,direccion5)

listaDoble = DoubleList()
listaDoble.addFirst(usuario1)
listaDoble.addLast(usuario2)
listaDoble.addLast(usuario3)
listaDoble.addLast(usuario4)
listaDoble.addLast(usuario5)

# Mostrando cada elemento de la lista
print("Elementos de la lista")
current_node = listaDoble.first()
while current_node is not None:
    print(current_node.getData())
    current_node = current_node.getNext()


##Usuario por consola 1
#Nombre y id
nombre6 = input("\nIngresa el el nombre de el nuevo usuario: ")
id6 = input("Ingrese el ID: ")
#Fecha
fecha_input6 = input('Introduzca su fecha de nacimiento en forma dd-mm-aa: ')
fecha_lista6 = fecha_input6.split('-')
fecha6 = Fecha(fecha_lista6[0],fecha_lista6[1],fecha_lista6[2])
#Ciudad de nacimiento, tel y email
ciudad6 = input("Introduzca su ciudad de nacimiento: ")
tel6 = int(input("Introduzca su número de teléfono: "))
email6 = input("Introduzca su E-mail: ")
#Dirección
print("\nDirección\n")
direccion_calle6 = input('Introduzca el nombre de la calle. Ej: "Calle82"  ')
direccion_numero6 = input('Introduzca el número: Ej:"50-23  ')
direccion_barrio6 = input ('Nombre del barrio: ')
direccion_ciudad6 = input('Ciudad: ')
direccion_edificio6 = input('Cuál es el nombre del edificio (opcional - si no tiene oprima enter): ')
direccion_apto6 = input('Escriba el apartamento o complemento (opcional - si no tiene oprima enter): ')
direccion6 = Direccion(direccion_calle6,direccion_numero6,direccion_barrio6,direccion_ciudad6,direccion_edificio6,direccion_apto6)

#creando el usuario
usuario6 = Usuario(nombre6,id6,fecha6,ciudad6,tel6,email6,direccion6)

##Usuario por consola 2
nombre7 = input("\nIngresa el el nombre de el nuevo usuario: ")
id7 = input("Ingrese el ID: ")
#Fecha
fecha_input7 = input('Introduzca su fecha de nacimiento en forma dd-mm-aa: ')
fecha_lista7 = fecha_input7.split('-')
fecha7 = Fecha(fecha_lista7[0],fecha_lista7[1],fecha_lista7[2])
#Ciudad de nacimiento, tel y email
ciudad7 = input("Introduzca su ciudad de nacimiento: ")
tel7 = int(input("Introduzca su número de teléfono: "))
email7 = input("Introduzca su E-mail: ")
#Dirección
print("\nDirección\n")
direccion_calle7 = input('Introduzca el nombre de la calle. Ej: "Calle82"  ')
direccion_numero7 = input('Introduzca el número: Ej:"50-23  ')
direccion_barrio7 = input ('Nombre del barrio: ')
direccion_ciudad7 = input('Ciudad: ')
direccion_edificio7 = input('Cuál es el nombre del edificio (opcional - si no tiene oprima enter): ')
direccion_apto7 = input('Escriba el apartamento o complemento (opcional- si no tiene oprima enter): ')
direccion7 = Direccion(direccion_calle7,direccion_numero7,direccion_barrio7,direccion_ciudad7,direccion_edificio7,direccion_apto7)

#creando el usuario
usuario7 = Usuario(nombre7,id7,fecha7,ciudad7,tel7,email7,direccion7)

#Añadiendolos a la lista
listaDoble.addFirst(usuario6)
listaDoble.addLast(usuario7)

# Mostrando cada elemento de la lista
print("Elementos de la lista")
current_node = listaDoble.first()
while current_node is not None:
    print(current_node.getData())
    current_node = current_node.getNext()

