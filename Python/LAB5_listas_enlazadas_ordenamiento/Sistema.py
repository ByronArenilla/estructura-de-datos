from collections import defaultdict
from Usuario import Usuario
from Bandeja_entrada import BandejaEntrada
from Direccion import Direccion
from Mensaje import Mensaje

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.bandejas = defaultdict(BandejaEntrada)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        self.ordenar_usuarios_por_cedula()

    def eliminar_usuario(self, cedula):
        self.usuarios = [usuario for usuario in self.usuarios if usuario.cedula != cedula]
        self.ordenar_usuarios_por_cedula()

    def cambiar_contrasena(self, cedula, nueva_contrasena):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                usuario.contrasena = nueva_contrasena
                break

    def autenticar_usuario(self, cedula, contrasena):
        for usuario in self.usuarios:
            if usuario.cedula == cedula and usuario.contrasena == contrasena:
                return usuario
        return None

    def enviar_mensaje(self, remitente, cedula_destinatario, titulo, contenido):
        destinatario = self.buscar_usuario_por_cedula(cedula_destinatario)
        if destinatario:
            mensaje = Mensaje(remitente.nombre, destinatario.nombre, titulo, contenido)
            self.bandejas[cedula_destinatario].agregar_mensaje(mensaje)
        else:
            print("Destinatario no encontrado")

    def buscar_usuario_por_cedula(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        return None

    def ordenar_usuarios_por_cedula(self):
        self.bubble_sort_usuarios()

    def bubble_sort_usuarios(self):
        n = len(self.usuarios)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.usuarios[j].cedula > self.usuarios[j+1].cedula:
                    self.usuarios[j], self.usuarios[j+1] = self.usuarios[j+1], self.usuarios[j]

def guardar_datos(self):
    # Guardar información de los empleados en "Empleados.txt"
    with open('Empleados.txt', 'w') as f_empleados:
        for usuario in self.usuarios:
            direccion = usuario.direccion
            direccion_str = f'{direccion.getCalle()} {direccion.getNomenclatura()} {direccion.getBarrio()} {direccion.getCiudad()} {direccion.getEdificio() or ""} {direccion.getApto() or ""}'
            f_empleados.write(f'{usuario.nombre},{usuario.cedula},{usuario.fecha_nacimiento},{usuario.ciudad_nacimiento},{direccion_str},{usuario.telefono},{usuario.correo}\n')

    # Guardar información de contraseñas en "Password.txt"
    with open('Password.txt', 'w') as f_passwords:
        for usuario in self.usuarios:
            f_passwords.write(f'{usuario.cedula},{usuario.contrasena},{usuario.rol}\n')
