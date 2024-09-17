from Chained_Hash import Chained_Hash
# Ejemplo de uso
m = 9  # Tamaño del arreglo
cadena = Chained_Hash(m, "division")
dato = 45  # Clave del dato para insertar
cadena.insertar(dato)

# Buscar un dato
cadena.buscar(45)

# Eliminar un dato
cadena.eliminar(45)
