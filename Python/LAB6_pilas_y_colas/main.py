from TurnoUsuario import TurnoUsuario
from Usuario import Usuario
#Creando los usuarios
usuario1 = Usuario("Byron","2293")
usuario2 = Usuario("Dani","7379")
usuario3 = Usuario("Annie","8765")
usuario4 = Usuario("Obelis","7474")
usuario5 = Usuario("Eduardo","9898")

#Creando los registros
turnos = TurnoUsuario()
turnos.registrar(usuario1)
turnos.registrar(usuario2)
turnos.registrar(usuario3)
turnos.registrar(usuario4)
turnos.registrar(usuario5)

# turnos.toFile()

turnos.atenderSiguiente()
turnos.atenderSiguiente()
turnos.toFile()