# Importar los módulos Problema3.py y Problema4.py
import Problema3
import Problema4

continuar = True

while continuar:
  print("Menú de opciones:")
  print("1. Calcular el área de un círculo")
  print("2. Calcular el área de un rectángulo")
  print("3. Calcular el área de un cuadrado")
  print("4. Salir")

  opcion = input("Ingrese una opción: ")

  if opcion == "1":
    radio = input("Ingrese el valor del radio del círculo: ")
    try:
      radio = float(radio)
      Circulo = Problema3.CIRCULO(radio)
      Circulo.area()
      print(f"El área del círculo es: {Circulo.area()}")
    except ValueError:
      print("El valor del radio no es válido. Por favor, ingrese un número.")
  elif opcion == "2":
    largo = input("Ingrese el valor del largo del rectángulo: ")
    ancho = input("Ingrese el valor del ancho del rectángulo: ")
    try:
      largo = float(largo)
      ancho = float(ancho)
      rectangulo = Problema4.RECTANGULO(largo, ancho)
      rectangulo.area()
      print(f"El área del rectángulo es: {rectangulo.area()}")
    except ValueError:
      print("Los valores del largo y el ancho no son válidos. Por favor, ingrese números.")
  elif opcion == "3":
    lado = input("Ingrese el valor del lado del cuadrado: ")
    try:
      lado = float(lado)
      cuadrado = Problema4.RECTANGULO(lado, lado)
      cuadrado.area()
      print(f"El área del cuadrado es: {cuadrado.area()}")
    except ValueError:
      print("El valor del lado no es válido. Por favor, ingrese un número.")
  elif opcion == "4":
    continuar = False
    print("Gracias por usar el menú. Hasta pronto.")
  else:
    print("Opción no válida. Intente de nuevo.")
