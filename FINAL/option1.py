from tabulate import tabulate

def list_top_songs(data):
    top_songs = data.nlargest(5, ["Likes", "Views", "Comments"])
    top_songs.index = top_songs.index + 2
    
    table = tabulate(top_songs[["Index", "Title", "Artist", "Likes", "Views", "Comments"]], headers="keys", tablefmt="pretty", showindex=False)
    
    print(table)
