"""Crea un juego donde el programa "piensa" un número secreto entre 1 y 100
(puedes definirlo estáticamente, por ejemplo, numero_secreto = 42). El usuario
debe adivinarlo. En cada intento, el programa le dirá si el número ingresado es
mayor o menor que el número secreto. El juego termina cuando el usuario adivina
el número."""

num=int(input("Ingrese un numero entre 1 y 100: "))
num_secreto= 67

if num>num_secreto:
    print(f"El numero secreto es menor")
elif num<num_secreto:
    print(f"El numero secreto es mayor")

