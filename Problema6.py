# Definir una clase llamada Producto
class Producto:
  def __init__(self, nombre, precio, marca, año):
    self.nombre = nombre
    self.precio = precio
    self.marca = marca
    self.año = año
  
  def display(self):
    print(f"Nombre: {self.nombre}")
    print(f"Precio: {self.precio}")
    print(f"Marca: {self.marca}")
    print(f"Año: {self.año}")

class Catalogo:
  def __init__(self):
    self.productos = []
  
  def agregar_producto(self, producto):
    self.productos.append(producto)
  
  def mostrar_productos(self):
    for producto in self.productos:
      producto.display()
      print("----------")
  
  def filtrar_por_año(self, año):
    filtrados = []
    for producto in self.productos:
      if producto.año == año:
        filtrados.append(producto)
    print(f"Los productos del año {año} son:")
    for producto in filtrados:
      producto.display()
      print("----------")
  
  def ordenar_por_precio(self):
    self.productos.sort(key=lambda producto: producto.precio)
    print("Los productos ordenados por precio de menor a mayor son:")
    for producto in self.productos:
      producto.display()
      print("----------")

catalogo = Catalogo()

cantidad = input("Ingrese la cantidad de productos que desea ingresar: ")

try:
  cantidad = int(cantidad)
  for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = input(f"Ingrese el precio del producto {i+1}: ")
    marca = input(f"Ingrese la marca del producto {i+1}: ")
    año = input(f"Ingrese el año del producto {i+1}: ")
    try:
      precio = float(precio)
      año = float(año)
      producto = Producto(nombre, precio, marca, año)
      catalogo.agregar_producto(producto)
    except ValueError:
      print("El precio o el año no son válidos. Por favor, ingrese números.")
  catalogo.mostrar_productos()
  año = input("Ingrese el año para filtrar los productos: ")
  try:
    año = float(año)
    catalogo.filtrar_por_año(año)
  except ValueError:
    print("El año no es válido. Por favor, ingrese un número.")
  catalogo.ordenar_por_precio()
except ValueError:
  print("La cantidad no es válida. Por favor, ingrese un número entero.")
