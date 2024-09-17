from Chained_Hash import Chained_Hash

m = 9  # Tamaño del arreglo
cadena = Chained_Hash(m, "division")
dato = 45  # Clave del dato para insertar
cadena.insertar(dato)
cadena.insertar(9)

# Buscar un dato
cadena.buscar(45)
cadena.buscar(9)

# Eliminar un dato
cadena.eliminar(45)
