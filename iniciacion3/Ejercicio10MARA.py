# -*- coding: utf-8 -*-
"""
Crea un programa que simule una tienda en línea y la interacción con un usuario. Para ello, se tendrá que poder realizar lo siguiente:
Se deberán poder agregar productos con nombre, stock y precio a la tienda. También se podrán actualizar el stock y el precio. Como esto únicamente lo puede hacer un administrador, se pedirá una clave para realizarlo.
Se podrán mostrar los productos disponibles de la tienda con su debido stock y precio.
Se podrán añadir productos al carrito si hay stock disponible.
Se podrán retirar productos del carrito.
Se podrá saber el contenido del carrito.
Se podrá saber el coste total del carrito.
Se podrá realizar la compra de dichos productos. NOTA: al final de cada compra se tiene que actualizar el stock en la tienda.
Cosas a tener en cuenta:
Se pueden utilizar las funciones que se crean necesarias para que el código quede lo más limpio y funcional posible.
Intenta tener en cuenta las distintas características del problema. Por ejemplo, un usuario no puede comprar más stock del disponible de un producto, a la hora de mostrar stock hay que tener en cuenta el carrito, etc.

"""
# Función que inicializa productos, carrito y clave de administrador
def tienda():
    productos = {"nombre": [], "stock": [], "precio": []}  # Listas de productos en tienda
    carrito = {"nombre": [], "cantidad": []}  # Carrito de compra
    claveAdmin = "admin123"  # Clave predeterminada para administrador
    return productos, carrito, claveAdmin

# Función que gestiona las acciones del administrador (agregar o modificar productos)
def administrador(productos, claveAdmin):
    claveIntroducida = input("Introduzca una clave de administrador: ")
    if claveIntroducida != claveAdmin:
        print("Clave incorrecta, intente de nuevo.")
    else:
        print("Opciones administrador")
        opcion = int(input("1. Agregar producto\n2. Modificar producto\nElige un numero: "))
        if opcion == 1:
            # Agregar un producto
            nombreProducto = input("Agrega un nombre: ")
            stockProducto = int(input("Agrega un stock: "))
            precioProducto = float(input("Agrega un precio: "))
            productos["nombre"].append(nombreProducto)
            productos["stock"].append(stockProducto)
            productos["precio"].append(precioProducto)
        elif opcion == 2:
            # Modificar stock y precio de un producto existente
            actNombreProducto = input("Dime el nombre a actualizar: ")
            if actNombreProducto in productos["nombre"]:
                indice = productos["nombre"].index(actNombreProducto)
                stockActualizado = int(input("Nuevo stock: "))
                precioActualizado = float(input("Nuevo precio: "))
                productos["stock"][indice] = stockActualizado
                productos["precio"][indice] = precioActualizado
    return productos, claveAdmin

# Función para agregar productos al carrito de compra
def agregarCarrito(productos, carrito):
    productoCarrito = input("Agrega un nombre al carrito: ")
    if productoCarrito not in productos["nombre"]:
        print("El producto no está en la tienda")
    else:
        cantidad = int(input("Cantidad a agregar: "))
        indice_producto = productos["nombre"].index(productoCarrito)
        if productos["stock"][indice_producto] < cantidad:
            print("Cantidad mayor que el stock")
        else:
            # Añadir al carrito
            carrito["nombre"].append(productoCarrito)
            carrito["cantidad"].append(cantidad)
    return productos, carrito

# Función para retirar productos del carrito
def retirarProductoCarrito(carrito):
    nombreRetiroCarrito = input("Producto a retirar del carrito: ")
    if nombreRetiroCarrito not in carrito["nombre"]:
        print("El producto no está en el carrito")
    else:
        indiceCarrito = carrito["nombre"].index(nombreRetiroCarrito)
        carrito["cantidad"][indiceCarrito] -= 1
        if carrito["cantidad"][indiceCarrito] == 0:
            del carrito["nombre"][indiceCarrito]
            del carrito["cantidad"][indiceCarrito]
    return carrito

# Función para calcular y mostrar el total del carrito
def TotalCarrito(productos, carrito):
    valorTotal = sum(carrito["cantidad"][i] * productos["precio"][i] for i in range(len(carrito["nombre"])))
    print("El valor total del carrito es " + str(valorTotal))
    return productos, carrito

# Función para realizar la compra y actualizar stock
def comprarCarrito(productos, carrito):
    totalCompra = 0
    for i, nombre in enumerate(carrito["nombre"]):
        indice = productos["nombre"].index(nombre)
        cantidad = carrito["cantidad"][i]
        precio = productos["precio"][indice]
        totalCompra += cantidad * precio
        productos["stock"][indice] -= cantidad  # Actualización de stock
    print(f"Compra realizada con éxito. Total: {totalCompra}€.")
    carrito["nombre"].clear()  # Limpiar el carrito
    carrito["cantidad"].clear()
    return productos, carrito

# Menú principal con las opciones disponibles para el usuario
print("Tienda")
print("1. Agregar o actualizar productos")
print("2. Mostrar productos")
print("3. Añadir al carrito")
print("4. Retirar del carrito")
print("5. Mostrar carrito")
print("6. Total carrito")
print("7. Comprar carrito")
print("8. Salir")

productos, carrito, claveAdmin = tienda()

# Bucle principal donde el usuario selecciona opciones del menú
while True:
    opcion = int(input("Elige un número: "))
    if opcion == 1:
        productos, claveAdmin = administrador(productos, claveAdmin)
    elif opcion == 2:
        print(productos)
    elif opcion == 3:
        productos, carrito = agregarCarrito(productos, carrito)
    elif opcion == 4:
        carrito = retirarProductoCarrito(carrito)
    elif opcion == 5:
        print(carrito)
    elif opcion == 6:
        productos, carrito = TotalCarrito(productos, carrito)
    elif opcion == 7:
        productos, carrito = comprarCarrito(productos, carrito)
    elif opcion == 8:
        print("Saliendo")
        break
