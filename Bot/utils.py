from imdb import IMDb
import re

imdb = IMDb()
LONG_IMDB_DESCRIPTION = False

async def get_title(query):
    query = (query.strip()).lower()
    title = query
    movieid = imdb.search_movie(title.lower(), results=10)
    if not movieid:
        return None
    filtered = movieid
    movieid=list(filter(lambda k: k.get('kind') in ['movie', 'tv series'], filtered))
    if not movieid:
        movieid = filtered
    movieid = movieid[0].movieID

    movie = imdb.get_movie(movieid)

    return {'title': movie.get('title')}
