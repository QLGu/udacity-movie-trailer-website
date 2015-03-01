class Movie():
    '''
    This class provides a way to store movie related infomation
    '''

    def __init__(self, title, year, storyline,
                 poster_image_url,
                 youtube_trailer_id):
        self.title = title
        self.year = year
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.youtube_trailer_id = youtube_trailer_id
