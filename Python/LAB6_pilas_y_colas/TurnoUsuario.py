from Queque import Queque
from Stack import Stack
class TurnoUsuario():
    def __init__(self):
        self.__registro = Queque()
        self.__usuarioAtendido = Stack()

    def registrar(self, u): #registrar un objeto tipo Usuario
        self.__registro.enqueque(u)

    def atenderSiguiente(self):
        if not self.__registro.isEmpty():  # Verifica que la cola no esté vacía
            usuario = self.__registro.dequeque()  # Saca el siguiente usuario de la cola
            self.__usuarioAtendido.push(usuario)  # Lo empuja a la pila de usuarios atendidos
            return usuario  # Retorna el usuario que fue atendido
        else:
            print("No hay más usuarios en la cola para atender.")
            return None  

    def toFile(self):
        usuariosAtendidos = open('usuariosatendidos.txt','w')
        while not self.__usuarioAtendido.isEmpty():
            usuario = self.__usuarioAtendido.pop()
            usuariosAtendidos.write(f"Id: {usuario.getId()}-Nombre : {usuario.getNombre()}\n")

        usuariosPendientes = open('usuariospendientes.txt','w')
        while not self.__registro.isEmpty():
            usuario = self.__registro.dequeque()
            usuariosPendientes.write(f"Id: {usuario.getId()}-Nombre: {usuario.getNombre()}\n")







