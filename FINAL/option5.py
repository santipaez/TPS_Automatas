from tabulate import tabulate

def list_longest_songs(data):
    data["Duration_min"] = data["Duration_ms"] / 60000
    top_longest_songs = data.nlargest(10, "Duration_min")
    
    table = []
    for index, row in top_longest_songs.iterrows():
        duration_min = int(row["Duration_min"])
        duration_sec = int((row["Duration_min"] - duration_min) * 60)
        duration_str = f"{duration_min:02}:{duration_sec:02}"
        table.append([index, row["Title"], duration_str])
    
    headers = ["Index", "Title", "Duration"]
    print(tabulate(table, headers=headers, tablefmt="pretty", showindex=False))
