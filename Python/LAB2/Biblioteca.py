from Fecha import Fecha
from Direccion import Direccion
from Usuario import Usuario

#Nombre y ID
nombre = input('Nombre: ')
id = input('ID: ')

#Fecha
fecha_input = input('Introduzca su fecha de nacimiento en forma dd-mm-aa: ')
fecha_lista = fecha_input.split('-')

fecha = Fecha(fecha_lista[0],fecha_lista[1],fecha_lista[2])

#Ciudad de nacimiento, tel y email
ciudad = input('Ciudad de nacimiento: ')
tel = input('Teléfono: ')
email = input('Email: ')


#Dirección
direccion_calle = input('Introduzca el nombre de la calle. Ej: "Calle82"  ')
direccion_numero = input('Introduzca el número: Ej:"50-23  ')
direccion_barrio = input ('Nombre del barrio: ')
direccion_ciudad = input('Ciudad: ')
direccion_edificio = input('Cuál es el nombre del edificio (opcional): ')
direccion_apto = input('Escriba el apartamento o complemento: ')

direccion = Direccion(direccion_calle,direccion_numero,direccion_barrio,direccion_ciudad,direccion_edificio,direccion_apto)



usuario = Usuario(nombre,id,fecha,ciudad,tel,email,direccion)
print(usuario.__str__())