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

##Usuario por consola 3
nombre8 = input("\nIngresa el el nombre de el nuevo usuario: ")
id8 = input("Ingrese el ID: ")
#Fecha
fecha_input8 = input('Introduzca su fecha de nacimiento en forma dd-mm-aa: ')
fecha_lista8 = fecha_input8.split('-')
fecha8 = Fecha(fecha_lista8[0],fecha_lista8[1],fecha_lista8[2])
#Ciudad de nacimiento, tel y email
ciudad8 = input("Introduzca su ciudad de nacimiento: ")
tel8 = int(input("Introduzca su número de teléfono: "))
email8 = input("Introduzca su E-mail: ")
#Dirección
print("\nDirección\n")
direccion_calle8 = input('Introduzca el nombre de la calle. Ej: "Calle82"  ')
direccion_numero8 = input('Introduzca el número: Ej:"50-23  ')
direccion_barrio8 = input ('Nombre del barrio: ')
direccion_ciudad8 = input('Ciudad: ')
direccion_edificio8 = input('Cuál es el nombre del edificio (opcional - si no tiene oprima enter): ')
direccion_apto8 = input('Escriba el apartamento o complemento (opcional- si no tiene oprima enter): ')
direccion8 = Direccion(direccion_calle8,direccion_numero8,direccion_barrio8,direccion_ciudad8,direccion_edificio8,direccion_apto8)

#creando el usuario
usuario8 = Usuario(nombre8,id8,fecha8,ciudad8,tel8,email8,direccion8)





# Encontrar el nodo en la posición deseada (posicón 3 en este caso)
nodo_actual = listaDoble.first()
posicion_actual = 1
while nodo_actual is not None and posicion_actual < 3:
    nodo_actual = nodo_actual.getNext()
    posicion_actual += 1
listaDoble.addAfter(nodo_actual,usuario8)



# Mostrando cada elemento de la lista
print("Elementos de la lista")
current_node = listaDoble.first()
while current_node is not None:
    print(current_node.getData())
    current_node = current_node.getNext()