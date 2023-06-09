
# Ejercicios estructuras repetitivas y estructuras condicionales.
# 1. Realice un programa que lea 4 números y diga cuántos son pares y
# cuantos impares y devuelva la sumatoria de los pares.

while True:
    # Leer 4 números
    numeros = []
    for i in range(4):
        num = int(input("Ingrese un número: "))
        numeros.append(num)

    # Contadores y sumatoria
    pares = 0
    impares = 0
    suma_pares = 0

    # Determinar cuántos son pares y cuántos impares, y calcular sumatoria de los pares
    for num in numeros:
        if num % 2 == 0:
            pares += 1
            suma_pares += num
        else:
            impares += 1

    # Mostrar resultados
    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)
    print("Sumatoria de los números pares:", suma_pares)

    # Preguntar si desea volver a empezar
    respuesta = input("¿Desea volver a empezar? (s/n): ")
    if respuesta.lower() != "s":
        break
