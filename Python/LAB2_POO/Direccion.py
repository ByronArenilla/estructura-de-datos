class Direccion:
    def __init__(self,calle,nomenclatura,barrio,ciudad,edificio = None,apto =None):
        self.__calle = calle
        self.__nomenclatura = nomenclatura 
        self.__barrio = barrio
        self.__ciudad = ciudad 
        self.__edificio = edificio
        self.__apto = apto 

    def getCalle(self):
        return self.__calle
    
    def setCalle(self,c):
        self.__calle = c

    def getNomenclatura(self):
        return self.__nomenclatura
    
    def setNomenclatura(self,n):
        self.__nomenclatura = n
    
    def getBarrio(self):
        return self.__barrio
    
    def setBarrio(self,b):
        self.__barrio = b
    
    def getCiudad(self):
        return self.__ciudad
    
    def setCiudad(self, ci):
        self.__ciudad = ci
    
    def getEdificio(self):
        return self.__edificio
    
    def setEdificio(self, e):
        self.__edificio = e
    
    def getApto(self):
        return self.__apto
    
    def setApto(self,a):
        self.__apto = a


    def __str__(self) :
        return f'{self.__calle} # {self.__nomenclatura} {self.__barrio}  {self.__ciudad} {self.__edificio or""} apto/complemento {self.__apto or""}'
    