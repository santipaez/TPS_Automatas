def list_best_ratio(data):
    data["Likes/Views Ratio"] = data["Likes"] / data["Views"]
    top_ratio_songs = data.nlargest(5, "Likes/Views Ratio")
    
    for index, row in top_ratio_songs.iterrows():
        print(f"{row['Title']} - {row['Likes/Views Ratio'] * 100:.2f}%")
