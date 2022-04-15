from time import time

from Bot import Sflix, script
from pyrogram import filters
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Sflix.on_message(filters.command("start") & filters.private)
async def start(client: Sflix, message: Message):
    await message.reply_text("Hi")

@Sflix.on_message(filters.command("movie") & filters.group)
async def movie(client: Sflix, message: Message):
    reply_to = message.reply_to_message
    if reply_to:
        admin_check = await client.get_chat_member(message.chat.id, reply_to.from_user.id)
        if ((admin_check.status == "administrator") or (admin_check.status == "creator")):
            await message.reply_text("**This user is admin in this chat.**")
            return

        reply_id = reply_to.message_id
        buttons = [[
            InlineKeyboardButton("Leave 🧑‍🦯", callback_data="movie.leave")
            ],[
            InlineKeyboardButton("Kick 🗑️", callback_data="movie.kick")
            ],[
            InlineKeyboardButton("Ignore ✨", callback_data="movie.ignore")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.delete()
        await message.reply_text(
            text = script.MOVIE_TXT.format(reply_to.from_user.mention),
            reply_markup = reply_markup,
            reply_to_message_id = reply_id
        )
    else:
        await message.reply("Reply")
