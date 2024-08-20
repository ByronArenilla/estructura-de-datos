class Usuario:
    def __init__(self, nombre, cedula, fecha_nacimiento, ciudad_nacimiento, direccion, telefono, correo, contrasena=None, rol=None):
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

    def es_admin(self):
        return self.rol == "administrador"

    def __str__(self):
        return f'{self.nombre} ({self.cedula})'
