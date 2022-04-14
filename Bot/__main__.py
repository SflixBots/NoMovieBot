from Bot import Sflix
from pyrogram import filters
from pyrogram.types import Message

@Sflix.on_message(filters.command("start") | filters.private)
async def start(client: Sflix, message: Message):
    await message.reply_text("Hi")

@Sflix.on_message(filters.regex("#movie") | filters.group)
async def movie(client: Sflix, message: Message):
    reply_to = message.reply_to_message
    if reply_to:
        reply_id = reply_to.message_id
        await message.reply_text()
