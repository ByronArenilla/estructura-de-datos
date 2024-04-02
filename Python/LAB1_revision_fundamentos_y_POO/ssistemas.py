import random
def lugar(tamaño):
  monedas=[12,50,94]
  return monedas

def dado():
  r=random.random()
  if r < 1/6:
    resu=1
  elif r < 2/6:
    resu=2
  elif r < 3/6:
    resu=3
  elif r < 4/6:
    resu=4
  elif r < 5/6:
    resu=5
  else:
    resu=6
  return resu

def juego(tamaño,posicion):
  p=0
  while p < tamaño:
    num=dado()
    p+=num
    if p in posicion:
      return True
  return False

NL=input('escriba el número de lanzamientos de dado\n')
N=int(NL)
def inicio():
  tamaño=100
  gana=0
  for n in range(N):
    posicion=lugar(tamaño)
    if juego(tamaño,posicion):
      gana+=1
