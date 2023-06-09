# Ejercicio estructura condicional simple:
# 1. Realice un programa que solicite dos letras ingresadas por el usuario y
# verifique si son iguales o no, mostrando un mensaje.

while True:
    letra1 = input("Ingrese la primera letra: ")
    letra2 = input("Ingrese la segunda letra: ")

    if letra1 == letra2:
        print("Las letras son iguales.")
    else:
        print("Las letras son diferentes.")

    respuesta = input("¿Desea volver a empezar? (s/n): ")
    if respuesta.lower() != "s":
        break
