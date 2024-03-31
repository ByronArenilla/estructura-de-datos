#Función del promedio
def promedio(lista):
    suma = 0
    for i in range(len(lista)):
        num = lista[i]
        suma += num
    return suma/len(lista)



#Asegurarme de que ingrese un entero
while True:
    try:
        N =int(input ("¿Cuántos números desea ingresar?: "))
        break
    except:
        print("Debe ingresar un entero")


listNum = []
for i in range(N):
    while True:
        try:
            num = int(input("ingrese el número: "))
            listNum.append(num)
            break
        except:
            print("Recuerda que debes ingresar un número entero")

    numMax= max(listNum)
    numMin = min(listNum)
    prom = promedio(listNum)
    suma = sum(listNum)
print(f"El valor máximo de la lista de números que ingresó es {numMax}. El valor mínimo es {numMin}. La suma de los numeros es {suma} y el valor promedio es {prom}")




