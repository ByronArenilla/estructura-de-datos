ruta = 'G:/Mi unidad/Semestre 2024-1/Estructura de Datos/Laboratorios/LAB 1/test_pr2.txt'
archivo = open(ruta)
lista = []
for line in archivo:
    linea = line.split()
    for palabra in linea:
        if palabra == 'el':
            lista.append(palabra)
print(f"La palabra 'en' se repite {len(lista)} veces en el texto")
