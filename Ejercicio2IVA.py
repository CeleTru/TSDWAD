"""  
Diseña un algoritmo que calcule el IVA (21%) de un producto solicitando al usuario su precio de venta sin IVA.
"""

# Solicitar al usuario el precio de venta sin IVA
precio_sin_iva = float(input("Ingrese el precio de venta sin IVA: "))

# Calcular el monto del IVA
iva = precio_sin_iva * 0.21

# Calcular el precio de venta con IVA
precio_con_iva = precio_sin_iva + iva

# Mostrar los resultados por pantalla
print("El monto del IVA (21% es) :", iva)
print("El precio de venta con IVA es:", precio_con_iva)
