"""Ejercicio 14: Simulador de Cajero Automático (ATM)
Crea un programa que simule las operaciones de un cajero automático. El
programa debe gestionar un saldo inicial.
• Debe encapsular la lógica en funciones como consultar_saldo(),
depositar(), retirar().
• Utiliza un bucle while para mantener el programa en ejecución hasta que el
usuario decida salir.
• Valida las operaciones (ej. no se puede retirar más dinero del que hay en el
saldo).
• El código debe ser claro, legible y seguir las recomendaciones de PEP 8.
• Conceptos integrados: Funciones, bucle while, condicionales, variables,
operadores, I/O, PEP 8."""

"""
Simulador de Cajero Automático.
Permite consultar saldo, depositar y retirar dinero.
"""

#  Variable global para el saldo
saldo = 0.0


def consultar_saldo():
    """
    Muestra el saldo actual.
    """
    print(f" Tu saldo actual es: ${saldo:.2f}\n")


def depositar():
    """
    Permite al usuario depositar una cantidad positiva en su cuenta.
    """
    global saldo
    try:
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        if cantidad > 0:
            saldo += cantidad
            print(f" Has depositado ${cantidad:.2f}. Nuevo saldo: ${saldo:.2f}\n")
        else:
            print(" El monto debe ser mayor que cero.\n")
    except ValueError:
        print(" Entrada inválida. Debe ingresar un número.\n")


def retirar():
    """
    Permite al usuario retirar dinero si tiene suficiente saldo.
    """
    global saldo
    try:
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad <= 0:
            print(" El monto debe ser mayor que cero.\n")
        elif cantidad > saldo:
            print(" Fondos insuficientes. No puedes retirar más que tu saldo.\n")
        else:
            saldo -= cantidad
            print(f" Has retirado ${cantidad:.2f}. Nuevo saldo: ${saldo:.2f}\n")
    except ValueError:
        print(" Entrada inválida. Debe ingresar un número.\n")


def mostrar_menu():
    """
    Muestra el menú principal y gestiona la selección del usuario.
    """
    while True:
        print("=== CAJERO AUTOMÁTICO ===")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break
        else:
            print(" Opción inválida. Intente de nuevo.\n")


#  Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu()
