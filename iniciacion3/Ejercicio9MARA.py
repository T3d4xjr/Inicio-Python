# Función para crear un inventario vacío
def inventario():
    inventory = {"nombre": [], "cantidad": [], "precio": []}
    return inventory

# Función para agregar un producto al inventario
def agregraProducto(inventory):
    # Pedimos datos del producto y los añadimos al inventario
    nombreProducto = input("Agrega un nombre: ")
    cantidadProducto = int(input("Agrega una cantidad: "))
    precioProducto = float(input("Agrega un precio: "))
    
    inventory["nombre"].append(nombreProducto)
    inventory["cantidad"].append(cantidadProducto)
    inventory["precio"].append(precioProducto)
   
    return inventory

# Función para actualizar la cantidad de un producto
def actualizarProducto(inventory):
    nombreProducto = input("Dime el nombre del producto a actualizar: ")
    if nombreProducto in inventory["nombre"]:
        indice = inventory["nombre"].index(nombreProducto)
        cantidadActualizada = int(input("Nueva cantidad: "))
        inventory["cantidad"][indice] = cantidadActualizada
    else:
        print("No existe el producto")
    
    return inventory

# Función para ver el valor de un producto
def valorInventarioProducto(inventory):
    nombreProducto = input("Dime el nombre del producto: ")
    if nombreProducto in inventory["nombre"]:
        indice = inventory["nombre"].index(nombreProducto)
        valorTotal = inventory["cantidad"][indice] * inventory["precio"][indice]
        print("Valor total: " + str(valorTotal))
    else:
        print("No existe el producto")
    
    return inventory

# Función para calcular el valor total del inventario
def valorInventarioTotal(inventory):
    valorTotal = sum(
        inventory["cantidad"][i] * inventory["precio"][i] for i in range(len(inventory["nombre"]))
    )
    print("Valor total del inventario: " + str(valorTotal))
    return inventory

# Inicializamos el inventario vacío
inventory = inventario()

# Menú principal
print("Inventario")
print("1. Agregar Producto")
print("2. Actualizar Producto")
print("3. Valor de producto")
print("4. Valor inventario total")
print("5. Mostrar inventario")
print("6. Salir")

while True:
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        inventory = agregraProducto(inventory)
    elif opcion == 2:
        inventory = actualizarProducto(inventory)
    elif opcion == 3:
        inventory = valorInventarioProducto(inventory)
    elif opcion == 4:
        inventory = valorInventarioTotal(inventory)
    elif opcion == 5:
        print(inventory)
    elif opcion == 6:
        print("Saliendo")
        break
