def search_song(data):
    search_term = input("Ingrese parte del título de la canción: ")

    # Llenar los valores NaN en la columna "Title" con una cadena vacía
    data["Title"].fillna('', inplace=True)

    # Filtrar las filas que contienen el término de búsqueda en el título
    result = data[data["Title"].str.contains(search_term, case=False, na=False)]
    
    if result.empty:
        print("No se encontraron canciones que coincidan con el término de búsqueda.")
    else:
        print(result)
