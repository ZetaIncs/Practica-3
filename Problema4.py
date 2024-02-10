# Definir una clase llamada RECTANGULO
class RECTANGULO:
  def __init__(self, largo, ancho):
    self.largo = largo
    self.ancho = ancho
  
  def area(self):
    return self.largo * self.ancho

largo = input("Ingrese el valor del largo del rectángulo: ")
ancho = input("Ingrese el valor del ancho del rectángulo: ")

try:
  largo = float(largo)
  ancho = float(ancho)
  rectangulo = RECTANGULO(largo, ancho)
  print(f"El área del rectángulo es: {rectangulo.area()}")
except ValueError:
  print("Los valores del largo y el ancho no son válidos. Por favor, ingrese números.")
