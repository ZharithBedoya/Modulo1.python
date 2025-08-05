"""Crea una función que reciba un texto (string) y devuelva un diccionario con la
frecuencia de cada palabra. El diccionario tendrá las palabras como claves y su
conteo como valor. No debe distinguir entre mayúsculas y minúsculas.
"""

# Función para contar la frecuencia de cada palabra
def contar_palabras(texto):
    # Convertimos el texto a minúsculas para no distinguir mayúsculas
    texto = texto.lower()

    # Separamos el texto en palabras
    palabras = texto.split()

    # Creamos un diccionario vacío para contar las palabras
    frecuencia = {}

    # Recorremos la lista de palabras
    for palabra in palabras:
        # Sumamos 1 si ya existe, o iniciamos en 1 si no existe
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia

# Pedimos al usuario que ingrese el texto
texto_usuario = input("Escribe un texto: ")

# Llamamos a la función con ese texto
resultado = contar_palabras(texto_usuario)

# Mostramos el resultado
print("\nFrecuencia de palabras:")
for palabra, cantidad in resultado.items():
    print(f"{palabra}: {cantidad}")

