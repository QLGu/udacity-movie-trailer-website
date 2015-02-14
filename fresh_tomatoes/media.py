class Movie():
    '''
    This class provides a way to store movie related infomation
    '''

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, storyline, poster_image_url, youtube_trailer_id):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.youtube_trailer_id = youtube_trailer_id
