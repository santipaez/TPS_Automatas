def list_top_artists(data):
    top_artists = data.groupby("Artist")["Views"].sum().reset_index()
    top_artists = top_artists.nlargest(10, "Views")
    
    for index, row in top_artists.iterrows():
        print(f"{row['Artist']} - {row['Views']}")
