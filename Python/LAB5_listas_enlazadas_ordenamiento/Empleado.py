from Direccion import Direccion

class Empleado:
    def __init__(self, nombre, cedula, fecha_nacimiento, ciudad_nacimiento, direccion, telefono, correo):
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f'{self.nombre}, {self.cedula}, {self.fecha_nacimiento}, {self.ciudad_nacimiento}, {self.direccion}, {self.telefono}, {self.correo}'
