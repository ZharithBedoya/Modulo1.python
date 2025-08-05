"""Crea una función que reciba una lista de calificaciones (números). La función
debe calcular y retornar el promedio, la calificación más alta y la más baja en una
tupla. Luego, escribe el código para probar esta función con una lista de ejemplo."""

def calificacion(numeros):  #se crea la funcion
    promedio=sum(numeros)/len(numeros)  #se crea la variable promedio y se le da la funcion de suma
                                      #las notas y se divide con la funcion len entre la cantidad de notas
    max_cal=max(numeros)              #se crea la variable max_cal y se le da funcion de mas para calcular la maxima nota
    min_cal=min(numeros)              #se crea la funcion min_cal y se le da la funcion min que se encarga de buscar la funcion minima
    return promedio,max_cal,min_cal #python los agrupa en una tupla por comas y devuelve varios valores a la vez
calificaciones=[] #crear una lista vacia para almacenar las calificaciones


num_notas=int(input("¿Cuantas notas desea ingresar?"))  #se crea la variable num_notas que almacena la cantidad de notas que desea ingresar el usuario

for i in range(num_notas):  #se crea un bucle
    while True:
        nota=float(input(f"Ingresa la nota {i+1}: ")) #impresion de mensajes para que ingrese la nota
        if nota <=0: #validar si la nota es menor de 0
            print("El nota debe ser mayor a 0")
        else:
            break # terminar el bucle while
    calificaciones.append(nota) #se encarga de agregar a la lista los valores ingresados
resultado=calificacion(calificaciones)
print(f"El promedio de la nota ingresada es: {resultado[0]:.2f}, la máxima nota es: {resultado[1]}, la mínima nota es: {resultado[2]}")