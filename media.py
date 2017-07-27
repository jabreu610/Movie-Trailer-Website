#!/usr/bin/env python


class Movie(object):
    """Class that describes the components of a Movie"""
    # Define constructor method

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        super(Movie, self).__init__()
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
