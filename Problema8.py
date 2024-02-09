import random

def generar_lista():
  lista = []
  for i in range(20):
    numero = random.randint(0, 100)
    lista.append(numero)
  return lista

def mostrar_lista(lista):
  print(lista)

def ordenar_lista(lista):
  lista.sort()
  print(lista)

