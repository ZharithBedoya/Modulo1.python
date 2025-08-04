"""Desarrolla un programa que permita al usuario gestionar una lista de compras. El
programa debe usar un bucle while para mostrar un menú con opciones:
1. Agregar ítem a la lista.
2. Eliminar ítem de la lista.
3. Ver la lista completa.
4. Salir. El programa debe gestionar la lista de compras y seguir las
instrucciones del usuario."""

lista = [] #se crea una lista vacia
opcion = 0  # se crea una variable opcion que inicia en 0
print("Lista de compras ")  # titulo de la consola
while opcion !=4:           #ciclo para que se repita mientras opcion no sea diferente de 4
    print("1.Agregar item a la lista\n2.Eliminar item de la lista\n3.Ver la lista completa\n4.Salir ")  # imprimir la lista
    opcion = int(input("Seleccione una opcion "))  # se guarda en la variable opcion la opcion que dijito el usuario

    if opcion == 1:  #si opcion es igual 1
        cant=int(input("¿Cuantos items desea agregar? ")) # guardar cuantos items desea ingresar el usuario
        for i in range(cant): #un ciclo para crear un rango y un iterador de acuerdo a la cantidad ingresada
           opcionlista=str(input(f"Agregar item {i+1} a la lista ")) #guardar en la variable opcionlista el item ingresado por el usuario
           lista.append(opcionlista) #esta funcion agrega el item a la lista


    elif opcion == 2:  #si la opcion es igual a 2
        if lista: #verifica si la lista contiene elementos
            print("Los ítems de la lista son:") #impresion
            for i, item in enumerate(lista, start=1): #recorre cada elemento de la lista iniciando desde 1
                print(f"{i}. {item}") #imprime el iterador con el nombre del item de la lista
            item_eliminar = input("Escriba el nombre exacto del ítem que desea eliminar: ") #escribr el nombre del item a eliminar y se almacena en la variable item_eliminar
            if item_eliminar in lista: #si item:eliminar esta en lista
                lista.remove(item_eliminar) #eliminar el valor ingresado
                print(f"'{item_eliminar}'  ha sido eliminado.") #imprimir el nombre del item
            else:
                print(f"'{item_eliminar}' este item no se encuentra en la lista.") #si el item no se encuentra en la lista imprimir
        else:
            print("La lista está vacía.") #en caso de la lista esta vacia


    elif opcion == 3: #si la opcion es 3
        if lista: #verifica que no este la lista vacia
            print("Los ítems de la lista son:") #imprimir
            for i, item in enumerate(lista, start=1): #recorre cada elemento iniciando desde 1
                print(f"{i}. {item}") #impresion


    elif opcion == 4:  #si la opcion es 4
        print("Saliendo...")  #imprimir
        exit() #cerrar el programa