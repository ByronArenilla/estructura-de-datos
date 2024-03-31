class Fecha:
    def __init__(self,dd,mm,aa):
        self.__dd = dd
        self.__mm = mm
        self.__aa = aa

    def getDia(self):
        return self.__dd
    
    def setDia(self,dd):
        self.__dd = dd

    def getMes(self):
        return self.__mm
    
    def setMes(self,mm):
        self.__mm = mm

    def getA(self):
        return self.__aa
    
    def setA(self,aa):
        self.__aa = aa
    
    def __str__(self):
        return (f'{self.__dd}-{self.__mm}-{self.__aa}')

# fecha = Fecha("25","Mar","2023")
# print(fecha.getDia())fecha = Fecha("25","Mar","2023")
# print(fecha.getDia())