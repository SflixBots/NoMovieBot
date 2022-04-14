from Bot import Config

from pyrogram.raw.all import layer
from pyrogram import Client, __version__

SESSION = Config.SESSION_NAME
API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN
WORKERS = Config.WORKERS

class Sflix(Client):
    #Starts the Pyrogram Client on the Bot Token when we do 'python3 bot_class.py'

    def __init__(self):
        super().__init__(
           session_name=SESSION,
           api_id=API_ID,
           api_hash=API_HASH,
           bot_token=BOT_TOKEN,
           workers=WORKERS,
           plugins={"root": "Bot"},
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
        print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")

bot = Sflix()
bot.run()
