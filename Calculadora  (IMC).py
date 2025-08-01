"""Crea un programa que pida al usuario su peso (en kg) y su altura (en metros).
Calcula el IMC usando la fórmula:
IMC=altura2peso
y muestre el resultado con un mensaje claro y formateado, redondeado a dos
decimales."""

peso=float(input("Digite su peso en Kg: ")) #almacenar el peso en la variable peso
print(f"Su peso es {peso}kg") #mostrar al usuario el peso que ha ingresado

altura=float(input("Digite su altura en metros: ")) #almacenar la altura en la variable altura
print(f"Su altura es {altura}m") #imprimir el valor de la variable altura

imc= peso/(altura**2) #almacenar en la variable imc la formula equivalente a imc

print(f"Su IMC es {imc:.2f}") #imprimir el valor de imc con 2 decimales