from lib.album_repository import *
from lib.album import *

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_album_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums[:4] == [
        Album('Doolittle', 1989, 1),
        Album('Surfer Rosa', 1988, 1),
        Album('Waterloo', 1974, 2),
        Album('Super Trouper', 1980, 2),
        ]

"""
When we call the find method with an id
We get the single record with that id
"""
def test_find_single_item(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    
    album = repository.find(3)
    assert album == Album("Waterloo", 1974, 2)

"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    new_album = Album("Another Mix", 2025, 1)
    repository.create(new_album)

    albums = repository.all()
    assert albums[-1] == Album("Another Mix", 2025, 1)