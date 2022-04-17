from os import environ
from pyrogram import Client

class Config:
    #Config class for variables.

    SESSION_NAME = "NoMovieBot"
    API_ID = int(environ['API_ID'])
    API_HASH = environ['API_HASH']
    BOT_TOKEN = environ['BOT_TOKEN']
    WORKERS = int(100)
    OMDB_KEY = environ.get("OMDB_KEY", "")

class script:
    START_TXT = """Hey There I'm {bot.first_name}

**I'm a User-Friendly group Management Bot**

⤜ **Awake Since:** `{uptime}`

Click **Help Commands** to know how to use me."""

    HELP_TXT = """Hi"""

    ABOUT_TXT = """
My name: Philip                
                
My creator: @Don_Sflix               
                
My language: Python               
                
My Library: Pyrogram 
               
My Source: <a href='https://github.com/SflixBots/NoMovieBot'>Click here</a>"""

    MOVIE_TXT = """Hello {}
Looks like you are asking a movie
But this is not a movie group! 👀
Now you can leave from here or admins will kick you."""

Sflix = Client
