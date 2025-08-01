"""Escribe un programa que solicite la edad del usuario y determine si es mayor de
edad o no. El programa debe mostrar un mensaje apropiado. Adicionalmente, si la
edad está entre 18 y 25 años, debe mostrar un mensaje indicando que es un "joven
adulto"."""

edad=(int(input("Digite su edad: ")))  #almacenar la variable edad
if edad>=1 and edad<18: #realizar la condicion si es menor de 18
    print(f"Usted es menor de edad porque tiene {edad} años") #imprimir si se cumple la condicion
elif edad >= 26 and edad <= 74:  # hacer condicion de edad mayor de 18
    print(f"Usted es mayor de edad porque tiene {edad} años")
elif edad >=18 and edad <= 25:  # imprimir usted es joven adulto si edad es mayor o igual a 18 y edad es menor o igual a 25
    print(f"Usted es joven adulto porque tiene {edad} años")
elif edad<=0:                               #si se ingresa un valor diferente imprimir una validacion
    print(f"Ingrese una edad valida, usted ingreso {edad} años y esa edad no es valida")

