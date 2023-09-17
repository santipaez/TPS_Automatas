# No se usan expresiones regulares y el index está mal (deberia ser 1149 en vez de 1147)
import constants

def list_top_songs(data):
    top_songs = data.nlargest(5, ["Likes", "Views", "Comments"])
    print(top_songs[["Title", "Artist", "Likes", "Views", "Comments"]].to_string(index=False))
