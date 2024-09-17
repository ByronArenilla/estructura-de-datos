from Chained_Hash_Usuario import Chained_Hash_Usuario
from Usuario import Usuario
from Fecha import Fecha
from Direccion import Direccion
m = 5 #Tabla hash con 5 posiciones
tabla_hash = Chained_Hash_Usuario(m,"division")

#Creando los usuarios
#Usuario 1
fecha = Fecha("23","03","2002")
direccion = Direccion("calle 82a","90a-10","Robledo","Medellín")
usuario = Usuario("Byron","10001992293",fecha,"Medellín","3148839303","byronarenilla7@gmail.com",direccion)

#Usuario 2
fecha2 = Fecha("1","4","2005")
direccion2 = Direccion("calle 83a","98-10","Lureles","Medellín")
usuario2 = Usuario("Annie","1013338765",fecha2,"Medellín","3224636761","annie@gmail.com",direccion2)


#Usuario 3
fecha3 = Fecha("11","12","1978")
direccion3 = Direccion("calle 45a","50-10","Belen","Medellín")
usuario3 = Usuario("Obelis","32007474",fecha3,"Medellín","3224636377","obelis@gmail.com",direccion3)

#usuario 4
fecha4 = Fecha("22","12","1978")
direccion4 = Direccion("calle 36a","45-22","Aranjuez","Medellín")
usuario4 = Usuario("Eduardo","71779898",fecha4,"Medellín","3207074917","eduardo@gmail.com",direccion4)

#Usuario 5
fecha5 = Fecha("7","10","1999")
direccion5 = Direccion("calle 70","64-10","Pilarica","Medellín")
usuario5 = Usuario("Daniela","1152717379",fecha5,"Medellín","3224686898","daniela@gmail.com",direccion5)

#Usuario 6
fecha6 = Fecha("29","04","1957")
direccion6 = Direccion("calle 37","90a-10","Estadio","Medellín")
usuario6 = Usuario("Emiro","71180392",fecha5,"Medellín","3103874438","emiro@gmail.com",direccion5)

#Insertando los usuarios a la tabla hash
tabla_hash.insertar(usuario)
tabla_hash.insertar(usuario2)
tabla_hash.insertar(usuario3)
tabla_hash.insertar(usuario4)
tabla_hash.insertar(usuario5)
tabla_hash.insertar(usuario6)

# Recorrer cada posición del arreglo
print("\n")
for i, lista in enumerate(tabla_hash.arreglo):
    if lista is None:
        print(f"Posición {i}: 0 usuarios")
    else:
        print(f"Posición {i}: {lista.size()} usuarios")


##Ahora lo mismo pero con el método de multiplicación
print("\nMétodo de multiplicación\n")
m = 5 #Tabla hash con 5 posiciones
tabla_hash_multiplicacion = Chained_Hash_Usuario(m,"multiplicacion")
#Insertando los usuarios a la tabla hash
tabla_hash_multiplicacion.insertar(usuario)
tabla_hash_multiplicacion.insertar(usuario2)
tabla_hash_multiplicacion.insertar(usuario3)
tabla_hash_multiplicacion.insertar(usuario4)
tabla_hash_multiplicacion.insertar(usuario5)
tabla_hash_multiplicacion.insertar(usuario6)

# Recorrer cada posición del arreglo
print("\n")
for i, lista in enumerate(tabla_hash.arreglo):
    if lista is None:
        print(f"Posición {i}: 0 usuarios")
    else:
        print(f"Posición {i}: {lista.size()} usuarios")

