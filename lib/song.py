class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    song_instances = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.__class__.add_song_to_count()
        self.__class__.add_to_genres(genre)
        self.__class__.add_to_artists(artist)
        self.__class__.song_instances.append(self)  # Add the instance to song_instances

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = {genre: 0 for genre in cls.genres}
        for song in cls.song_instances:
            cls.genre_count[song.genre] += 1

    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count = {artist: 0 for artist in cls.artists}
        for song in cls.song_instances:
            cls.artist_count[song.artist] += 1