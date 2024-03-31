usPass = {
    "Juan123": "J12an*",
    "Maria2345": "M23a",
    "Pablo1459": "P140*",
    "Ana3456" : "A34a*"
}

maxIntentos = 3

for intento in range(maxIntentos):
    ingresaUsuario = input("Ingrese su nombre de usuario: ")
    ingresaPass = input("Ingrese su contraseña: ")

    if ingresaUsuario in usPass and usPass[ingresaUsuario] == ingresaPass:
        print("Acceso permitido")
        break
    else:
        print("Datos incorrectos")

    if intento == maxIntentos - 1:
        print("Lo siento, su acceso no es permitido")