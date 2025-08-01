"""Pide al usuario un número entero y muestra la tabla de multiplicar de ese número
del 1 al 10. El formato de salida debe ser claro, por ejemplo: 5 x 1 = 5."""

num=int(input("Ingrese un numero entero: ")) #almacenaer la variable ingresada

for cont in range(1,11):  #recorar del 1 al 10 en la variable cont
    print(f"{num} x {cont} = {num * cont}")  #realizar la impresion
