import re

def listar_top_canciones():
    # Abre y lee el archivo "Listado temas 2023"
    with open("Listado temas 2023.csv", "r") as archivo:
        lineas = archivo.readlines()

    # Define el patrón de expresión regular para una línea de datos
    patron = r'\d+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,[^,]+,\d+\.\d+,\d+\.\d+,\d+,-\d+\.\d+,\d+\.\d+,\d+\.\d+,\d+\.\d+,\d+\.\d+,\d+\.\d+,\d+\.\d+,\d+,\d+,[^,]+,[^,]+,\d+,\d+,\d+,[^,]+,[^,]+,\d+'

    # Inicializa una lista para almacenar los datos de las canciones
    datos = []

    # Procesa las líneas del archivo
    for linea in lineas[1:]:  # Ignora la primera línea (cabecera)
        match = re.match(patron, linea.strip())
        if match:
            campos = match.group().split(',')
            cancion = {
                "Artist": campos[1],
                "Track": campos[3],
                "likes": int(campos[23]),
                "views": int(campos[22]),
                "comentarios": int(campos[24])
            }
            datos.append(cancion)

    # Ordena las canciones por likes de mayor a menor
    canciones_ordenadas = sorted(datos, key=lambda x: x["likes"], reverse=True)

    # Toma las primeras 5 canciones (las de mayor cantidad de likes)
    top_canciones_likes = canciones_ordenadas[:5]

    # Imprime el resultado
    print("Las 5 canciones con más likes son:")
    for i, cancion in enumerate(top_canciones_likes, start=1):
        print(f"{i}. {cancion['Track']} - {cancion['Artist']} (Likes: {cancion['likes']}, Vistas: {cancion['views']}, Comentarios: {cancion['comentarios']})")
