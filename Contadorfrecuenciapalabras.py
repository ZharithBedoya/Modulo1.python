"""Desarrolla una función que reciba dos listas y devuelva una tupla con tres
conjuntos (sets):
1. Un conjunto con los elementos que están en ambas listas.
2. Un conjunto con los elementos que solo están en la primera lista.
3. Un conjunto con los elementos que solo están en la segunda lista."""

#
def comparar_listas(lista1, lista2): #definir la funcion que se encarga de coprarar las listas y devolver 3 conjuntos
    set1 = set(lista1)  # Convertimos la primera lista a conjunto
    set2 = set(lista2)  # Convertimos la segunda lista a conjunto

    en_ambas = set1 & set2            # Elementos que están en ambas listas
    solo_en_primera = set1 - set2     # Solo en la primera
    solo_en_segunda = set2 - set1     # Solo en la segunda

    return (en_ambas, solo_en_primera, solo_en_segunda)

#  Entrada de datos desde el usuario
entrada1 = input("Ingrese los elementos de la PRIMERA lista, separados por comas: ")
entrada2 = input("Ingrese los elementos de la SEGUNDA lista, separados por comas: ")

#  Convertimos la entrada en listas, quitando espacios
lista1 = [x.strip() for x in entrada1.split(",")]
lista2 = [x.strip() for x in entrada2.split(",")]

#  Llamamos a la función
resultado = comparar_listas(lista1, lista2)

#  Mostramos los resultados
print("\n📌 Resultados:")
print("1. Elementos en ambas listas:", resultado[0])
print("2. Elementos solo en la primera lista:", resultado[1])
print("3. Elementos solo en la segunda lista:", resultado[2])


