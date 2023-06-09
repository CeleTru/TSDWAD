# 4. Leer 10 números y mostrar solamente los números positivos, y su
# sumatoria.
import random

while True:
    numeros = []

    # Generar 10 números aleatorios
    for _ in range(10):
        numero = random.randint(-100, 100)
        numeros.append(numero)

    # Mostrar los números a analizar
    print("Estos son los 10 números a analizar:")
    for numero in numeros:
        print(numero, end=" ")

    # Filtrar y sumar los números positivos
    numeros_positivos = [num for num in numeros if num > 0]
    sumatoria_positivos = sum(numeros_positivos)

    # Mostrar los números positivos y su sumatoria
    print("\nNúmeros positivos:")
    for num in numeros_positivos:
        print(num, end=" ")
    print("\nSumatoria de los números positivos:", sumatoria_positivos)

    # Preguntar si desea volver a empezar
    respuesta = input("¿Desea volver a empezar? (s/n): ")
    if respuesta.lower() != "s":
        break
