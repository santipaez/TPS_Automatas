def list_longest_songs(data):
    data["Duration_min"] = data["Duration_ms"] / 60000
    top_longest_songs = data.nlargest(10, "Duration_min")
    
    for index, row in top_longest_songs.iterrows():
        duration_min = int(row["Duration_min"])
        duration_sec = int((row["Duration_min"] - duration_min) * 60)
        print(f"{row['Title']} - {duration_min:02}:{duration_sec:02}")
