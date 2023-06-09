 # 7. Diseña un algoritmo creando una tupla que almacene 3 categorías
# de música y luego crea un diccionario donde utilices como clave la
#  tupla y almacenes 2 músicos por categoría de música.
# Luego mostrar en pantalla los artistas.

while True:
    categorias = ("Rock", "Pop", "Electrónica")
    musicos = {
        categorias[0]: ("The Rolling Stones", "Led Zeppelin"),
        categorias[1]: ("Michael Jackson", "Madonna"),
        categorias[2]: ("Daft Punk", "Avicii")
    }

    print("Artistas por categoría de música:")
    for categoria, artistas in musicos.items():
        print("Categoría:", categoria)
        print("Artistas:", ", ".join(artistas))
        print()

    respuesta = input("¿Desea volver a empezar? (s/n): ")
    if respuesta.lower() != "s":
        break
