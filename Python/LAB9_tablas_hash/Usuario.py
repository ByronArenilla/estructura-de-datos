class Usuario:
    def __init__(self,nombre,id,fecha_nacimiento,ciudad_nacimiento,tel,email,dir):
        self.__nombre = nombre
        self.__id = id
        self.__fecha_nacimiento = fecha_nacimiento
        self.__ciudad_nacimiento = ciudad_nacimiento
        self.__tel  = tel
        self.__email = email
        self.__dir = dir

    #Get
    def getNombre(self):
        return self.__nombre

    def getId(self):
        return self.__id
    
    def getFecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    def getCiudad_nacimiento(self):
        return self.__ciudad_nacimiento
    
    def getTel(self):
        return self.__tel
    
    def getEmail(self):
        return self.__email
    
    def getDir(self):
        return self.__dir
    
    #Set

    def setNombre(self,n):
        self.__nombre = n
    
    def setId(self,id):
        self.__id = id
    
    def setFecha_nacimiento(self,f):
        self.__fecha_nacimiento = f 
    
    def setCiudad_nacimiento(self,c):
        self.__ciudad_nacimiento = c
    
    def setTel(self,t):
        self.__tel = t 
    
    def setEmail(self,e):
        self.__email = e 
    
    def setDir(self,d):
        self.__dir = d
    
    def __repr__(self):
        return f'''Usuario: {self.__nombre} \n
        ID: {self.__id} \n
        F.Nacimiento: {self.__fecha_nacimiento} \n
        C.Nacimiento: {self.__ciudad_nacimiento} \n
        Tel: {self.__tel} \n
        Email: {self.__email} \n
        Dirección: {self.__dir} \n'''