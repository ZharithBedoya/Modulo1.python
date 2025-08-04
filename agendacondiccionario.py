"""Crea un programa que simule una agenda de contactos. Utiliza un diccionario
donde las claves sean los nombres de los contactos y los valores sean sus
números de teléfono. Implementa funciones para:
1. Añadir un nuevo contacto.
2. Buscar el teléfono de un contacto por su nombre.
3. Mostrar todos los contactos."""


agenda = {} #Diccionario que se va encargar de almacenar los contactos
opc=0

while opc !=3: # mientras que opcion no sea diferente de 3
    print("Agenda de Contactos")
    opc = int(input("Digite:\n1.Para añadir un nuevo contacto\n2.Para buscar el telefono de un contacto por su nombre\n3.Para mostrar todos los contactos\nSeñor usuario digite el numero del menu anterior "))
      #almacenar en opc la opciion digitada
    if opc==1:
        entrada = (input("Para agregar su contacto ingrese el nombre y el telefono ejemplo:(Nombre,telefono) ")) #almacenar el contacto con nombre y telefono en entrada
        if "," in entrada: # si hay una , en agenda
            nombre,telefono = entrada.split(",", 1) #split elimina espacios en blanco, y separa cada variable con , una vez
            agenda[nombre.strip()] = telefono.strip() #guarda el contacto en agenda y uusa el nombre como clkave y telefono como valor
            print(f"Contacto '{nombre.strip()}' añadido con éxito.\n")
        else:
            print("Formato incorrecto. Use 'Nombre,Telefono'\n")
    if opc==2:
        contacto=str(input("Para encontrar el numero de contacto ingrese su nombre ")).lower() #.lower ignora las mayusculas y minusculas
        if contacto in agenda: #si contacto esta en agenda
            print(f"El número de {contacto} es {agenda[contacto]}\n")
        else:
            print("Contacto no encontrado.\n")

    if opc==3:
        print("Los contactos que se encuentran en la agenda son: ")
        for i in agenda:
            print(f"{i.title()}: {agenda[i]}") #coloca en mayuscula cada palabra

