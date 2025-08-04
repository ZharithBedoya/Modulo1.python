"""Escribe una función que reciba una palabra o frase y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda),
ignorando espacios y mayúsculas/minúsculas. La función debe retornar True o
False."""

palindromo=str(input("Ingresa una frase o palabra: ")) #pide al usuario la frase o la palabre y la guarda en palindromo
texto_limpio=palindromo.replace(" ", "").lower() #a la variable palindromo le reemplaza los espacios por vacios
if texto_limpio == texto_limpio[::-1]: #se compara si el texto limpio es igual de reversa
    print(f"{palindromo} es un palindromo") #se imprime que es un apalindromo
else: #sino
    print(f"{palindromo} no es un palindromo") #no es un palindromo