import re
import pandas as pd

def add_new_song(data):
    artist = input("Ingrese el nombre del artista: ")
    url_spotify = input("Ingrese la URL de Spotify del artista: ")
    track = input("Ingrese el nombre de la canción: ")
    album = input("Ingrese el nombre del álbum: ")
    album_type = input("Ingrese el tipo de álbum: ")
    url = input("Ingrese la URL de Spotify de la canción: ")
    duration_ms = input("Ingrese la duración en milisegundos: ")
    url_youtube = input("Ingrese la URL de YouTube: ")
    title = input("Ingrese el título de Youtube: ")

    if not re.match(r'^https:\/\/open\.spotify\.com\/[a-zA-Z0-9/?=_]+$', url_spotify):
        print("URL de Spotify no válida.")
        return

    if not re.match(r'^\d+$', duration_ms):
        print("Duración no válida.")
        return

    if not re.match(r'^https:\/\/www\.youtube\.com\/watch\?v=[a-zA-Z0-9_-]+(&[a-zA-Z0-9_=&-]+)?$', url_youtube):
        print("URL de YouTube no válida.")
        return

    new_song = pd.DataFrame({
        "Artist": [artist],
        "Url_spotify": [url_spotify],
        "Track": [track],
        "Album": [album],
        "Album_type": [album_type],
        "Uri": [url],
        "Duration_ms": [int(duration_ms)],
        "Url_youtube": [url_youtube],
        "Title": [title]
    })

    data = pd.concat([data, new_song], ignore_index=True)
    
    data.to_excel("songs2023.xlsx", index=False, engine="openpyxl")
    print("Canción agregada exitosamente.")
