

class Song:

    count = 0
    artists = []
    artist_count = {}
    genres = []
    genre_count = {}
    song_list = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.increment_song_count()
        self.add_song_to_list(name)
        self.add_artist_to_list(artist)
        self.update_genres(genre)
        self.update_genres_count(genre)
        self.update_artist_count(artist)

    @classmethod
    def increment_song_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_song_to_list(cls, song):
        cls.song_list.append(song)

    @classmethod
    def add_artist_to_list(cls, artist):
        if (artist in cls.artists):
            print(f'{artist} already in list')
        else:
            cls.artists.append(artist)

    @classmethod
    def update_genres(cls, genre):
        if (genre in cls.genres):
            print(f'{genre} is already in the list')
        else:
            cls.genres.append(genre)

    @classmethod
    def update_genres_count(cls, genre):
        if (genre in cls.genre_count):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def update_artist_count(cls, artist):
        if (artist in cls.artist_count):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
