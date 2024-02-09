# Solicitar al usuario una lista de calificaciones separadas por comas
calificaciones = input("Ingrese una lista de calificaciones separadas por comas: ")

try:
  lista = calificaciones.split(",")
  enteros = []
  for elemento in lista:
    decimal = float(elemento)
    entero = round(decimal)    
    enteros.append(entero)
  print(f"La lista de calificaciones enteras es: {enteros}")
except ValueError:
  print("La lista de calificaciones no tiene el formato correcto. Por favor, ingrese solo números separados por comas.")
