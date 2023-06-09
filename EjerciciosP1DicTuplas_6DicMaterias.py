# 6. Diseña un algoritmo con un diccionario que contenga como clave 3
#  materias que estás cursando y como valores uses tuplas para almacenar
#  2 notas por materia. Luego por pantalla muestres las notas de cada
# materia.

while True:
    materias = {
        'Matemáticas': (8.5, 7.9),
        'Física': (6.7, 9.2),
        'Química': (7.8, 8.3)
    }

    print("Notas por materia:")
    for materia, notas in materias.items():
        print("Materia:", materia)
        print("Notas:", notas)
        print()

    respuesta = input("¿Desea volver a empezar? (s/n): ")
    if respuesta.lower() != "s":
        break
