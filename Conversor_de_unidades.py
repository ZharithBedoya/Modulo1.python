"""Escribe un programa que utilice un diccionario para almacenar factores de
conversión (ej: de metros a pies). Luego, crea una función que reciba una
cantidad, la unidad de origen y la unidad de destino, y realice la conversión. La
función debe manejar el caso en que una unidad no exista en el diccionario."""

# Diccionario con factores de conversión a metros
factores_conversion = {"metro": 1,"kilometro": 1000,"centimetro": 0.01,"milimetro": 0.001,"pulgada": 0.0254,"pie": 0.3048,"yarda": 0.9144,"milla": 1609.34}

# Función para convertir unidades
def convertir(cantidad, origen, destino):
    # Convertimos a minúsculas para evitar errores por mayúsculas
    origen = origen.lower()
    destino = destino.lower()

    # Verificamos si ambas unidades están en el diccionario
    if origen in factores_conversion and destino in factores_conversion:
        # Convertimos la cantidad a metros
        cantidad_en_metros = cantidad * factores_conversion[origen]

        # Convertimos de metros a la unidad destino
        resultado = cantidad_en_metros / factores_conversion[destino]

        return resultado
    else:
        # Si alguna unidad no está, mostramos error
        return " Unidad no válida. Revisa las unidades disponibles."

#  Ejemplo de uso
cantidad = float(input("Ingrese la cantidad a convertir: "))
unidad_origen = input("Ingrese la unidad de origen: ")
unidad_destino = input("Ingrese la unidad de destino: ")

# Realizar conversión
resultado = convertir(cantidad, unidad_origen, unidad_destino)

#  Mostrar resultado
if isinstance(resultado, str):
    print(resultado)  # Mensaje de error
else:
    print(f"{cantidad} {unidad_origen} equivalen a {resultado:.4f} {unidad_destino}")
