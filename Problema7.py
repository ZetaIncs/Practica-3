# Definir una clase llamada Punto
class Punto:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  
  def __str__(self):
    return f"({self.x},{self.y})"
  
  def cuadrante(self):
    if self.x == 0 and self.y == 0:
      print("El punto está sobre el origen.")
    elif self.x == 0 and self.y != 0:
      print("El punto está sobre el eje Y.")
    elif self.x != 0 and self.y == 0:
      print("El punto está sobre el eje X.")
    elif self.x > 0 and self.y > 0:
      print("El punto está en el primer cuadrante.")
    elif self.x < 0 and self.y > 0:
      print("El punto está en el segundo cuadrante.")
    elif self.x < 0 and self.y < 0:
      print("El punto está en el tercer cuadrante.")
    elif self.x > 0 and self.y < 0:
      print("El punto está en el cuarto cuadrante.")
  
  def vector(self, otro):
    vx = otro.x - self.x
    vy = otro.y - self.y
    print(f"El vector resultante es: ({vx},{vy})")

x = input("Ingrese la coordenada X del punto: ")
y = input("Ingrese la coordenada Y del punto: ")

try:
  x = float(x)
  y = float(y)
  punto = Punto(x, y)
  print(f"El punto es: {punto}")
  punto.cuadrante()
except ValueError:
  print("Las coordenadas no son válidas. Por favor, ingrese números.")

x2 = input("Ingrese la coordenada X del otro punto: ")
y2 = input("Ingrese la coordenada Y del otro punto: ")

try:
  x2 = float(x2)
  y2 = float(y2)
  otro = Punto(x2, y2)
  print(f"El otro punto es: {otro}")
  punto.vector(otro)
except ValueError:
  print("Las coordenadas no son válidas. Por favor, ingrese números.")
