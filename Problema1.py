# Solicitar al usuario una fracción con formato X/Y
fraccion = input("Ingrese una fracción con formato X/Y: ")

try:
  x, y = fraccion.split("/")
  x = int(x)
  y = int(y)
  if x <= y and y != 0:
    porcentaje = round(x/y * 100)
    if porcentaje < 1:
      print("E")
    elif porcentaje > 99:
      print("F")
    else:
      print(f"{porcentaje}%")
  else:
    print("La fracción no es válida. Por favor, ingrese otra fracción.")
except ValueError:
  print("La fracción no tiene el formato correcto. Por favor, ingrese solo números enteros.")
except ZeroDivisionError:
  print("No se puede dividir por cero. Por favor, ingrese otra fracción.")
