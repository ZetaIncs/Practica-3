import Problema9

a = input("Ingrese el primer valor: ")
b = input("Ingrese el segundo valor: ")

try:
  a = float(a)
  b = float(b)
  print(f"La suma de {a} y {b} es: {Problema9.suma(a, b)}")
  print(f"La resta de {a} y {b} es: {Problema9.resta(a, b)}")
  print(f"El producto de {a} y {b} es: {Problema9.producto(a, b)}")
  print(f"La división de {a} y {b} es: {Problema9.division(a, b)}")
except ValueError:
  print("Los valores no son válidos. Por favor, ingrese números.")
