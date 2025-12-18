from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager!")
        print("What would you like to do?")
        print("1 - List all albums")
        print("2 - List all artists")
        print("3 - Find album by artist")
        choice = input("Enter your choice: ")

        if choice == "1":
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            for album in albums:
                print(f"{album.id}: {album.title} ({album.release_year})")

        elif choice == "2":
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")

        elif choice == "3":
            artist_repository = ArtistRepository(self._connection)
            album_repository = AlbumRepository(self._connection)
            artists = artist_repository.all()
            for artist in artists:
                print(f"{artist.id}: {artist.name}")
            
            artist_id = input("Enter the artist id: ")
            albums = album_repository.find_by_artist(artist_id)
            for album in albums:
                print(f"{album.title} ({album.release_year})")

        else:
            print("Invalid choice, please select 1 or 2.")