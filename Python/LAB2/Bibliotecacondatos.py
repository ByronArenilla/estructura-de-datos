from Fecha import Fecha
from Direccion import Direccion
from Usuario import Usuario

fecha = Fecha("23","03","2002")
print(fecha.__str__())


direccion = Direccion("calle 82a","90a-10","Robledo","Medellín")
print(direccion.__str__())

usuario = Usuario("Byron","10001992293",fecha,"Medellín","3148839303","byronarenilla7@gmail.com",direccion)
print(usuario.__str__())
