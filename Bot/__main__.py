from Bot import Sflix
from pyrogram import filters
from pyrogram.types import Message

@Sflix.on_message(filters.command("start") | filters. private)
async def start(client: Sflix, message: Message):
    await message.reply_text("Hi")
