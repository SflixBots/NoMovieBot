from os import environ

class Config:
    #Config class for variables.

    SESSION_NAME = "NoMovieBot"
    API_ID = int(environ['API_ID'])
    API_HASH = environ['API_HASH']
    BOT_TOKEN = environ['BOT_TOKEN']
    WORKERS = int(100)