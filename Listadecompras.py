"""Desarrolla un programa que permita al usuario gestionar una lista de compras. El
programa debe usar un bucle while para mostrar un menú con opciones:
1. Agregar ítem a la lista.
2. Eliminar ítem de la lista.
3. Ver la lista completa.
4. Salir. El programa debe gestionar la lista de compras y seguir las
instrucciones del usuario."""
from select import select

lista = []
opcion = 0
print("Lista de compras ")
while opcion !=4:
    print("1.Agregar item a la lista\n2.Eliminar item de la lista\n3.Ver la lista completa\n4.Salir ")
    opcion = int(input("Seleccione una opcion "))

    if opcion == 1:
        cant=int(input("¿Cuantos items desea agregar? "))
        for i in range(cant):
           opcionlista=str(input(f"Agregar item {i+1} a la lista "))
           lista.append(opcionlista)


    elif opcion == 2:
        if lista:
            print("Los ítems de la lista son:")
            for i, item in enumerate(lista, start=1):
                print(f"{i}. {item}")
            item_eliminar = input("Escriba el nombre exacto del ítem que desea eliminar: ")
            if item_eliminar in lista:
                lista.remove(item_eliminar)
                print(f"'{item_eliminar}'  ha sido eliminado.")
            else:
                print(f"'{item_eliminar}' este item no se encuentra en la lista.")
        else:
            print("La lista está vacía.")


    elif opcion == 3:
        if lista:
            print("Los ítems de la lista son:")
            for i, item in enumerate(lista, start=1):
                print(f"{i}. {item}")


    elif opcion == 4:
        print("Saliendo...")
        exit()