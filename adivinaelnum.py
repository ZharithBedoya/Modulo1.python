"""Crea un juego donde el programa "piensa" un número secreto entre 1 y 100
(puedes definirlo estáticamente, por ejemplo, numero_secreto = 42). El usuario
debe adivinarlo. En cada intento, el programa le dirá si el número ingresado es
mayor o menor que el número secreto. El juego termina cuando el usuario adivina
el número."""

num_secreto= 67 #el numero secreto sera 67
num=int(input("Ingrese un numero entre 1 y 100: ")) #ingresar el numero entre 1 y 100

while num != num_secreto:
    if num>num_secreto: #condicion si el numero ingresado es maytor que el numero ingresado imprima
        print(f"El numero secreto es menor")  #este mensaje
    elif num<num_secreto:       # condicion si el numero ingresado es menor que el numero secreto
        print(f"El numero secreto es mayor") #imprimir este mensaje

    num = int(input("Intenta de nuevo, ingresa un número entre 1 y 100: "))  #nuevamente pregunta el numero y valida

print(f"¡Felicidades! Adivinaste el número secreto {num_secreto}") #si se adivina el numero imprime el mensaje
