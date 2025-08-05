"""Este es el proyecto final que integra todo. Escribe un script de Python que haga lo
siguiente:
1. Define una estructura de datos principal: un diccionario de estudiantes.
Las claves serán los nombres de los estudiantes y los valores serán listas
con sus calificaciones.
2. Crea una función calcular_promedio(calificaciones) que reciba una lista de
números y devuelva su promedio.
3. Crea una función obtener_estado(promedio) que devuelva "Aprobado" si el
promedio es mayor o igual a 3.0, y "Reprobado" en caso contrario.
4. Crea una función principal generar_reporte(estudiantes) que itere sobre el
diccionario de estudiantes. Para cada uno, debe llamar a las funciones
anteriores e imprimir un reporte formateado, como:
5. Reporte de Calificaciones:
6. -------------------------
7. - Estudiante: Ana, Promedio: 4.5, Estado: Aprobado
8. - Estudiante: Juan, Promedio: 2.8, Estado: Reprobado
9. -------------------------
10. Todo el script debe estar comentado, con docstrings en cada función
explicando qué hace, qué recibe y qué devuelve. La nomenclatura de
variables y funciones debe seguir PEP 8."""

"""
Proyecto Final - Reporte de Calificaciones de Estudiantes

Este script define una estructura de datos para almacenar calificaciones de estudiantes,
calcula su promedio, determina su estado (Aprobado o Reprobado), y genera un reporte.
"""


# Diccionario principal: estudiantes y sus calificaciones
estudiantes = {
    "Ana": [4.5, 3.8, 5.0],
    "Juan": [2.8, 2.5, 3.0],
    "María": [3.5, 4.0, 3.2],
    "Pedro": [1.5, 2.0, 2.8]
}


def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.

    Parámetros:
        calificaciones (list): Lista de números (floats o ints).

    Retorna:
        float: Promedio de las calificaciones.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def obtener_estado(promedio):
    """
    Determina si un estudiante aprueba o reprueba según su promedio.

    Parámetros:
        promedio (float): Promedio del estudiante.

    Retorna:
        str: "Aprobado" si promedio >= 3.0, "Reprobado" si es menor.
    """
    if promedio >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"


def generar_reporte(estudiantes):
    """
    Genera un reporte de calificaciones para cada estudiante.

    Parámetros:
        estudiantes (dict): Diccionario con nombres como claves y listas de calificaciones como valores.

    Retorna:
        None. Imprime el reporte en pantalla.
    """
    print("\n Reporte de Calificaciones:")
    print("-" * 35)

    for nombre, calificaciones in estudiantes.items():
        promedio = calcular_promedio(calificaciones)
        estado = obtener_estado(promedio)
        print(f"- Estudiante: {nombre}, Promedio: {promedio:.2f}, Estado: {estado}")

    print("-" * 35)


# Ejecutar el programa principal
if __name__ == "__main__":
    generar_reporte(estudiantes)
