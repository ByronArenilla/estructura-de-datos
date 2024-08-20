from Node import Node
from Lista import Lista
class Stack():
    def __init__(self):
        self.__data = Lista()
    def size(self):
        return self.__data.size()
    def isEmpty(self):
        return self.size() == 0
    def push(self,e):
        self.__data.addFirst(e)
    def pop(self):
        return self.__data.removeFirst()
    def top(self):
        if not self.isEmpty():
            return self.__data.first().getData()
        else:
            return None