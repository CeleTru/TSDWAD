# 5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos
# números.
import random

while True:
    numeros = []

    # Generar 15 números aleatorios negativos
    for _ in range(15):
        numero = random.randint(-100, -1)
        numeros.append(numero)

    # Mostrar los números a analizar
    print("Estos son los 15 números a analizar:")
    for numero in numeros:
        print(numero, end=" ")

    # Convertir los números negativos a positivos
    numeros_positivos = [abs(num) for num in numeros]

    # Mostrar los números positivos
    print("\nNúmeros positivos:")
    for num in numeros_positivos:
        print(num, end=" ")

    # Preguntar si desea volver a empezar
    respuesta = input("¿Desea volver a empezar? (s/n): ")
    if respuesta.lower() != "s":
        break
