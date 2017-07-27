#!/usr/bin/env python
from fresh_tomatoes import *
from media import Movie
import json

# Loads json and creates a list of Movie objects


def main():
    with open('favorite_movies.json') as content:
        data = json.load(content)
    movies = map(create_movie, data)
    open_movies_page(movies)

# Takes movie dictionary as parameter and returns Movie object


def create_movie(movie_dict):
    return Movie(movie_dict.get('title'), movie_dict.get('poster_image_url'), movie_dict.get('trailer_youtube_url'))


if __name__ == '__main__':
    main()
