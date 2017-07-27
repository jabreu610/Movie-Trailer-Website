#!/usr/bin/env python


class Movie(object):
    """Define a Movie object.

        Keyword arguments:
        title -- The title of the movie
        poster_image_url -- a url to an image of the poster art for the movie
        trailer_youtube_url -- a url to a trailer of the movie on YouTube
    """
    # Define constructor method

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        super(Movie, self).__init__()
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
