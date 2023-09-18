import pandas as pd, constants as const, os, time
from option1 import list_top_songs; from option2 import list_best_ratio
from option3 import search_song; from option4 import add_new_song
from option5 import list_longest_songs; from option6 import list_top_artists

os.system('cls')
print(f"{const.BLUE}Leyendo archivo...")

data = pd.read_excel("songs2023.xlsx")

os.system('cls')
        
while True:
    print(f"{const.BLUE}")
    print("Menú de Opciones:")
    print("1. Listar las 5 canciones con más likes, vistas y comentarios")
    print("2. Listar las 5 canciones con mejor ratio (likes/view), mostrar el porcentaje")
    print("3. Buscar una canción (puedo poner solo una parte)")
    print("4. Agregar nueva fila")
    print("5. Listar las 10 canciones que más duración tienen y mostrar cual es el tiempo en formato legible (MM:SS)")
    print("6. Listar los 10 artistas con más reproducciones en total")
    print("7. Salir")
    print(f"{const.RESET}")

    option = input("Seleccione una opción: ")

    if option == "1":
        print(f"{const.GREEN}")
        list_top_songs(data)
        print(f"{const.RESET}")
        time.sleep(3)
    elif option == "2":
        print(f"{const.GREEN}")
        list_best_ratio(data)
        print(f"{const.RESET}")
        time.sleep(3)
    elif option == "3":
        print(f"{const.GREEN}")
        search_song(data)
        print(f"{const.RESET}")
        time.sleep(3)
    elif option == "4":
        print(f"{const.GREEN}")
        add_new_song(data)
        print(f"{const.RESET}")
        time.sleep(3)
    elif option == "5":
        print(f"{const.GREEN}")
        list_longest_songs(data)
        print(f"{const.RESET}")
        time.sleep(3)
    elif option == "6":
        print(f"{const.GREEN}")
        list_top_artists(data)
        print(f"{const.RESET}")
        time.sleep(3)
    elif option == "7":
        break
    else:
        print("Opción no válida. Intente nuevamente.")
        time.sleep(3)
