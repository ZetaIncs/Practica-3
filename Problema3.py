# Importar el módulo math para usar la constante pi
import math

# Definir una clase llamada CIRCULO
class CIRCULO:
  def __init__(self, radio):
    self.radio = radio
  
  def area(self):
    return math.pi * self.radio ** 2

radio = input("Ingrese el valor del radio del círculo: ")

try:
  radio = float(radio)
  circulo = CIRCULO(radio)
  print(f"El área del círculo es: {circulo.area()}")
except ValueError:
  print("El valor del radio no es válido. Por favor, ingrese un número.")
