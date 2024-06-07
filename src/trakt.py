import requests
import json

def get_collections():
    headers = {
        'Content-Type': 'application/json',
        'trakt-api-version': '2',
        'trakt-api-key': '378b93c3631d02211bb8ed3d9ff0946c1b59a1f7fafdd2da847dc9068b9646da'
    }

    movie_response = requests.get("https://api.trakt.tv/users/leo1305/collection/movies", headers=headers)
    movies = []
    for movie in json.loads(movie_response.content):        
        movies.append(movie['movie'])

    show_response = requests.get("https://api.trakt.tv/users/leo1305/collection/shows", headers=headers)
    shows = []
    for show in json.loads(show_response.content):
        shows.append(show['show'])

    return movies + shows

    