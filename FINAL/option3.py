from tabulate import tabulate

def search_song(data):
    search_term = input("Ingrese parte del título de la canción: ")
    result = data[data["Title"].str.contains(search_term, case=False, na=False)]
    
    table = tabulate(result[["Index", "Artist", "Title"]], headers="keys", tablefmt="pretty", showindex=False)
    
    print(table)
