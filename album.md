```sql
Table: albums
Columns: title, release_year, artist_id

TRUNCATE TABLE albums RESTART IDENTITY;

INSERT INTO albums (title, release_year, artist_id) VALUES ('Doolittle', 1989, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Surfer Rosa', 1988, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Waterloo', 1974, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Super Trouper', 1980, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Bossanova', 1990, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Lover', 2019, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Folklore', 2020, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('I Put a Spell on You', 1965, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Baltimore', 1978, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Here Comes the Sun', 1971, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Fodder on My Wings', 1982, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Ring Ring', 1973, 2);

class Album: 
    def __init__(self):
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id 

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass

class AlbumRepository(self, connection):
    def all(self):
        pass 
    
