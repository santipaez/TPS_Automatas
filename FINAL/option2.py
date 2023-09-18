from tabulate import tabulate

def list_best_ratio(data):
    data["Likes/Views Ratio"] = data["Likes"] / data["Views"]
    top_ratio_songs = data.nlargest(5, "Likes/Views Ratio")
    
    table = tabulate(top_ratio_songs[["Index", "Title", "Likes/Views Ratio"]], headers="keys", tablefmt="pretty", showindex=False)
    
    print(table)
