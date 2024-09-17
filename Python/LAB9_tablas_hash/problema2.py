from Chained_Hash import Chained_Hash
import random

m = 10 #elementos de la tabla
tabla_hash = Chained_Hash(m,"division")
#creando e insertando los 20 números aleatorios

# Generar 20 números aleatorios entre 0 y 100
numeros_aleatorios = [random.randint(0, 100) for _ in range(20)]
print(numeros_aleatorios)

#Insertando cada número aleatorio
for i in numeros_aleatorios:
    tabla_hash.insertar(i)

#buscando uno de los números generados
print("\n")
tabla_hash.buscar(numeros_aleatorios[0])

#Eliminando uno de los números generados
print("\n")
tabla_hash.eliminar(numeros_aleatorios[5])

##Lo mismo pero con el método de multiplicación
print("\nMétodo de multiplicación")
tabla_hash_multiplicacion = Chained_Hash(m,"multiplicación")

#creando e insertando los 20 números aleatorios

# Generar 20 números aleatorios entre 0 y 100
numeros_aleatorios = [random.randint(0, 100) for _ in range(20)]
print(numeros_aleatorios)

#Insertando cada número aleatorio
for i in numeros_aleatorios:
    tabla_hash.insertar(i)

#buscando uno de los números generados
print("\n")
tabla_hash.buscar(numeros_aleatorios[0])

#Eliminando uno de los números generados
print("\n")
tabla_hash.eliminar(numeros_aleatorios[5])