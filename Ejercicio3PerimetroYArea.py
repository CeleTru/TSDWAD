"""
Diseña un programa que, a partir de solicitar al usuario el valor del lado de un cuadrado, muestre el valor de 
su perímetro (en metros) y el de su área (en metros).
"""

# Solicitar al usuario el valor del lado del cuadrado
lado = float(input("Ingrese el valor del lado del cuadrado (en metros): "))

# Calcular el perímetro del cuadrado
perimetro = 4 * lado

# Calcular el área del cuadrado
area = lado * lado

# Mostrar los resultados por pantalla
print("El perímetro del cuadrado es:", perimetro, "metros")
print("El área del cuadrado es:", area, "metros cuadrados")
