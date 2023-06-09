"""Diseña un algoritmo para calcular el área de un círculo solicitando al usuario su radio."""

import math

# Solicitar al usuario el valor del radio
radio = float(input("Ingrese el valor del radio del círculo: "))

# Calcular el área del círculo
area = math.pi * radio ** 2

# Mostrar el resultado por pantalla
print("El área del círculo es:", area)
