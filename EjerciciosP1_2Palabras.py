# 2. Hacer un programa que permita decidir si dos palabras son iguales o
 # diferentes. Mostrar mensaje por pantalla.

while True:
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    if palabra1 == palabra2:
        print("Las palabras son iguales.")
    else:
        print("Las palabras son diferentes.")

    respuesta = input("¿Desea volver a empezar? (s/n): ")
    if respuesta.lower() != "s":
        break
