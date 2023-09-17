import pandas as pd
from option1 import list_top_songs
from option2 import list_best_ratio
from option3 import search_song
from option4 import add_new_song
from option5 import list_longest_songs
from option6 import list_top_artists
import os, constants

# Cargar el archivo Excel
data = pd.read_excel("songs2023.xlsx")

while True:
    print(f"{constants.BLUE}")
    print("Menú de Opciones:")
    print("1. Listar las 5 canciones con más likes, vistas y comentarios")
    print("2. Listar las 5 canciones con mejor ratio (likes/view), mostrar el porcentaje")
    print("3. Buscar una canción (puedo poner solo una parte)")
    print("4. Agregar nueva fila")
    print("5. Listar las 10 canciones que más duración tienen y mostrar cual es el tiempo en formato legible (MM:SS)")
    print("6. Listar los 10 artistas con más reproducciones en total")
    print("7. Salir")
    print(f"{constants.RESET}")

    option = input("Seleccione una opción: ")

    if option == "1":
        print(f"{constants.GREEN}")
        list_top_songs(data)
        print(f"{constants.RESET}")
    elif option == "2":
        print(f"{constants.GREEN}")
        list_best_ratio(data)
        print(f"{constants.RESET}")
    elif option == "3":
        print(f"{constants.GREEN}")
        search_song(data)
        print(f"{constants.RESET}")
    elif option == "4":
        print(f"{constants.GREEN}")
        add_new_song(data)
        print(f"{constants.RESET}")
    elif option == "5":
        print(f"{constants.GREEN}")
        list_longest_songs(data)
        print(f"{constants.RESET}")
    elif option == "6":
        print(f"{constants.GREEN}")
        list_top_artists(data)
        print(f"{constants.RESET}")
    elif option == "7":
        break
    else:
        print("Opción no válida. Intente nuevamente.")
