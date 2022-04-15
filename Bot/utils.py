from imdb import IMDb

imdb = IMDb()

async def get_title(query):
    query = (query.strip()).lower()
    title = query
    movieid = imdb.search_movie(title.lower(), results=10)
    if not movieid:
        return None
    filtered = movieid
    if not movieid:
        movieid = filtered
    movieid = movieid[0].movieID

    movie = imdb.get_movie(movieid)

    return {'poster': movie.get('full-size cover url')}
