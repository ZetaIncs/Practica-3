# Definir una clase llamada Alumno
class Alumno:
  def __init__(self, nombre, numero):
    self.nombre = nombre
    self.numero = numero
  
  def display(self):
    print(f"Nombre: {self.nombre}")
    print(f"Número de registro: {self.numero}")
    print(f"Edad: {self.edad}")
    print(f"Nota: {self.nota}")
  
  def setAge(self, edad):
    self.edad = edad
  
  def setNota(self, nota):
    self.nota = nota

nombre = input("Ingrese el nombre del alumno: ")

numero = input("Ingrese el número de registro del alumno: ")

alumno = Alumno(nombre, numero)

edad = input("Ingrese la edad del alumno: ")

try:
  edad = int(edad)
  alumno.setAge(edad)
except ValueError:
  print("La edad no es válida. Por favor, ingrese un número entero.")

nota = input("Ingrese la nota del alumno: ")

try:
  nota = float(nota)
  alumno.setNota(nota)
except ValueError:
  print("La nota no es válida. Por favor, ingrese un número.")

alumno.display()
