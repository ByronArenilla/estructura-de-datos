from Lista import Lista
from Node import Node
class Queque():
    def __init__(self):
        self.__data = Lista()
    def size(self):
        return self.__data.size()
    def isEmpty(self):
        return self.size() == 0
    def enqueque(self, e):
        self.__data.addLast(e)
    def dequeque(self):
        return self.__data.removeFirst()
    def first(self):
        return self.__data.first().getData()
