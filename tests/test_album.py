from lib.album import *

"""
Album constructs with a title, release year and artist id
"""
def test_album_constructs():
    album = Album("Test Title", 1234, 5)
    assert album.title == "Test Title"
    assert album.release_year == 1234
    assert album.artist_id == 5

""" 
Two identical albums will be equal
"""
def test_album_can_be_equal():
    album1 = Album("Test Title", 1234, 5)
    album2 = Album("Test Title", 1234, 5)
    assert album1 == album2


"""
we can format album title to strings
"""
def test_albums_can_format_content(): 
    album = Album("Test Title", 1234, 5)
    assert str(album) == "Album(Test Title, 1234, 5)"