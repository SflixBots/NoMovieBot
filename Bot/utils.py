import requests

from Bot import Config

API_KEY = Config.OMDB_KEY

user = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57"}

async def get_title(query):
    try:
        url = f'http://www.omdbapi.com/?apikey={API_KEY}&t={text}'
        resp = requests.get(url, headers=user).json()
        title = resp['Title']
    except Exception as e:
        print(e)
    except KeyError:
        return
    return title
