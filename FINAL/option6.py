from tabulate import tabulate

def list_top_artists(data):
    top_artists = data.groupby("Artist")["Views"].sum().reset_index()
    top_artists = top_artists.nlargest(10, "Views")
    
    table = tabulate(top_artists, headers="keys", tablefmt="pretty", showindex=False)
    
    print(table)
