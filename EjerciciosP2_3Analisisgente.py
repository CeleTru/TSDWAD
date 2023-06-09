# 3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son
# mujeres, cuántos varones, cuántos mayores de edad y cuántos
# menores de edad.

import random

while True:
    edades = []
    sexos = []

    # Ingresar las edades y sexos de 15 personas de manera aleatoria
    for _ in range(15):
        edad = random.randint(1, 100)
        sexo = random.choice(["M", "F"])

        edades.append(edad)
        sexos.append(sexo)

    # Mostrar los datos en pantalla
    print("Datos de las 15 personas:")
    for i in range(15):
        print("Persona", i+1, "- Edad:", edades[i], "- Sexo:", sexos[i])

    # Calcular cantidad de mujeres, varones, mayores y menores de edad
    mujeres = sexos.count("F")
    varones = sexos.count("M")
    mayores_edad = sum(1 for edad in edades if edad >= 18)
    menores_edad = sum(1 for edad in edades if edad < 18)

    # Mostrar los resultados
    print("Cantidad de mujeres:", mujeres)
    print("Cantidad de varones:", varones)
    print("Cantidad de mayores de edad:", mayores_edad)
    print("Cantidad de menores de edad:", menores_edad)

    # Preguntar si desea volver a empezar
    respuesta = input("¿Desea volver a empezar? (s/n): ")
    if respuesta.lower() != "s":
        break
