# Leer 10 números y obtener la cantidad de mayores y la cantidad de
# menores a 100, cuál es el número máximo y cuál es el número mínimo.

import random

while True:
    # Generar 10 números aleatorios
    numeros = [random.randint(1, 200) for _ in range(10)]

    # Escribir los números
    print("Estos son los 10 números a analizar:")
    print(numeros)

    # Inicializar variables
    mayores_100 = 0
    menores_100 = 0
    numero_maximo = float('-inf')
    numero_minimo = float('inf')

    # Analizar los números
    for num in numeros:
        if num > 100:
            mayores_100 += 1
        elif num < 100:
            menores_100 += 1

        if num > numero_maximo:
            numero_maximo = num

        if num < numero_minimo:
            numero_minimo = num

    # Mostrar resultados
    print("Cantidad de números mayores a 100:", mayores_100)
    print("Cantidad de números menores a 100:", menores_100)
    print("Número máximo:", numero_maximo)
    print("Número mínimo:", numero_minimo)

    # Preguntar si desea volver a empezar
    respuesta = input("¿Desea volver a empezar? (s/n): ")
    if respuesta.lower() != "s":
        break

