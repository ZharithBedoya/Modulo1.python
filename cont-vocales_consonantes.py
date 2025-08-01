"""Desarrolla un programa que pida al usuario una frase. El programa debe contar
cuántas vocales y cuántas consonantes contiene la frase (sin contar espacios ni
símbolos) y mostrar los resultados."""

frase=str(input("Ingrese una frase: ").lower()) #se pide la frase y se convierte a minuscula
vocales="aeiou".lower() #almacenar las vocales en la variable vocales y con lower omiten mayusculas y minisculas
cont_vocales=0  #contador de vocalse y se inicia en 0
consonantes="bcdfghjklmnpqrstuvwxyz".lower() #almacena las consonantes  y lower omite mayusculas y minusculas
cont_consonantes=0 #contador de consonantes se inicia en 0

for letra in frase:  #ciclo for y se encarga de correrar letra por letra de la frase
    if letra in vocales: #valida que letras estan dentro de vocales
       cont_vocales += 1 # si es cumple que sume una a cont
    elif letra in consonantes: # valida que lertas son consonantes
         cont_consonantes += 1 #cuenta las consonante si se comple la sentencia
print(f"La frase tiene {cont_vocales} vocales y {cont_consonantes} consonantes")
