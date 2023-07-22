class Song:

    count = 0
    genres = []
    artists = []
    genre_count ={}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count(name, artist, genre)

    def add_song_to_count(self, name, artist, genre):
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        Song.count +=1

    def add_to_genres(self, genre):
        if  (genre not in Song.genres):
            Song.genres.append(genre)
            Song.genre_count[genre] = 0

        self.add_to_genre_count(genre)

    def add_to_artists(self, artist):  
        if  (artist not in Song.artists):
            Song.artists.append(artist)
            Song.artist_count[artist] = 0
        
        self.add_to_artist_count(artist)

    def add_to_genre_count(self, genre):
        Song.genre_count[genre]+=1

    def add_to_artist_count(self, artist):
        Song.artist_count[artist]+=1

