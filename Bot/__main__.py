from Bot import Sflix
from pyrogram import filters
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Sflix.on_message(filters.command("start") | filters.private)
async def start(client: Sflix, message: Message):
    await message.reply_text("Hi")

@Sflix.on_message(filters.regex("#movie") | filters.group)
async def movie(client: Sflix, message: Message):
    reply_to = message.reply_to_message
    if reply_to:
        reply_id = reply_to.message_id
        buttons = [[
            InlineKeyboardButton("Leave 🧑‍🦯", callback_data="movie.leave")
            ],[
            InlineKeyboardButton("Kick 🗑️", callback_data="movie.kick")
            ],[
            InlineKeyboardButton("Ignore", callback_data="movie.ignore")
        ]]
        await message.reply_text(
            text = script.MOVIE_TXT,
            reply_markup = reply_markup,
            reply_to_message_id=reply_id
        )
    else:
        await message.reply("Reply")
