from Mensaje import Mensaje

class BandejaEntrada:
    def __init__(self):
        self.mensajes = []

    def agregar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    def mostrar_mensajes(self):
        for i, mensaje in enumerate(self.mensajes):
            print(f"{i}. {mensaje.fecha} - {mensaje.titulo} de {mensaje.remitente}")

    def leer_mensaje(self, indice):
        if 0 <= indice < len(self.mensajes):
            print(self.mensajes[indice].contenido)
        else:
            print("Mensaje no encontrado")
