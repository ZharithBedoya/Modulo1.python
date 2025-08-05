"""Diseña un sistema para gestionar el inventario de una tienda. El inventario se
almacenará en una lista de diccionarios. Cada diccionario representará un
producto con "nombre", "precio" y "cantidad". El programa debe:
• Usar funciones para cada operación: agregar_producto(), realizar_venta(),
mostrar_inventario().
• La función realizar_venta debe actualizar la cantidad del producto vendido.
• El código debe estar bien documentado con docstrings y seguir la
nomenclatura de PEP 8.
• Mostrar un menú interactivo para el usuario."""

"""
Sistema de gestión de inventario para una tienda.
Cada producto se representa como un diccionario con nombre, precio y cantidad.
"""

# Lista para almacenar el inventario
inventario = []

def agregar_producto():
    """
    Agrega un nuevo producto al inventario.
    Pide al usuario el nombre, precio y cantidad del producto.
    """
    nombre = input("Ingrese el nombre del producto: ").strip()
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    producto = {
        "nombre": nombre.lower(),
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print(f" Producto '{nombre}' agregado correctamente.\n")


def realizar_venta():
    """
    Realiza una venta de un producto.
    Pide el nombre del producto y la cantidad vendida,
    y actualiza la cantidad en el inventario.
    """
    nombre = input("Ingrese el nombre del producto que desea vender: ").strip().lower()
    cantidad_vendida = int(input("Ingrese la cantidad a vender: "))

    for producto in inventario:
        if producto["nombre"] == nombre:
            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] -= cantidad_vendida
                total = producto["precio"] * cantidad_vendida
                print(f" Venta realizada. Total: ${total:.2f}\n")
                return
            else:
                print(" No hay suficiente stock para esta venta.\n")
                return

    print(" Producto no encontrado en el inventario.\n")


def mostrar_inventario():
    """
    Muestra la lista completa de productos en el inventario con nombre, precio y cantidad.
    """
    if not inventario:
        print(" El inventario está vacío.\n")
    else:
        print(" Inventario actual:")
        for producto in inventario:
            print(f"- {producto['nombre'].title()} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
        print()


def mostrar_menu():
    """
    Muestra el menú interactivo y maneja la selección del usuario.
    """
    while True:
        print("=== MENÚ DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            realizar_venta()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")


# Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu()
