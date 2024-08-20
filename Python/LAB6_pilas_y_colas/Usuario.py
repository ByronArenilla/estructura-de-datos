class Usuario:
    def __init__(self,nombre,id):
        self.__nombre = nombre
        self.__id = id


    #Get
    def getNombre(self):
        return self.__nombre

    def getId(self):
        return self.__id
    


    #Set

    def setNombre(self,n):
        self.__nombre = n
    
    def setId(self,id):
        self.__id = id
    

    
    
    def __repr__(self): #To String
        return f'{self.__nombre}/{self.__id}/'