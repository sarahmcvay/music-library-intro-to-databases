class Album: 
    def __init__(self, title, release_year, artist_id):
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def __eq__(self, other):
        # return self.__dict__ == other.__dict__
        if not isinstance(other, Album):
            return False 
        return (
            self.title == other.title and
            self.release_year == other.release_year and
            self.artist_id == other.artist_id
        )
    
    def __repr__(self):
        return f"Album({self.title}, {self.release_year}, {self.artist_id})"