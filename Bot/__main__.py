from time import time
from asyncio import sleep

from Bot import Sflix, script
from pyrogram import filters
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram.errors import RPCError

@Sflix.on_message(filters.command("start") & filters.private)
async def start(client: Sflix, message: Message):
    await message.reply_text("Hi")

@Sflix.on_message(filters.regex("#movie") & filters.group)
async def movie(client: Sflix, message: Message):
    reply_to = message.reply_to_message
    if reply_to:
        admin_check = await client.get_chat_member(message.chat.id, reply_to.from_user.id)
        if ((admin_check.status == "administrator") or (admin_check.status == "creator")):
            await message.reply_text("**This user is admin in this chat.**")
            return

        user_id = reply_to.from_user.id
        reply_id = reply_to.message_id
        buttons = [[
            InlineKeyboardButton("Leave 🧑‍🦯", callback_data=f"movie.leave.{user_id}")
            ],[
            InlineKeyboardButton("Kick 🗑️", callback_data=f"movie.kick.{user_id}")
            ],[
            InlineKeyboardButton("Ignore ✨", callback_data=f"movie.ignore.{user_id}")
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

@Sflix.on_callback_query(filters.regex("^movie."))
async def who_ask_for_movie(client: Sflix, query: CallbackQuery):
    args = query.data.split(".")
    action = args[1]
    user_id = int(args[2])
    chat_id = int(query.message.chat.id)
    user = await client.get_users(user_id)
    user_name = user.username

    if action == "leave":
        clicked = query.from_user.id
        typed = user_id

        if int(clicked) == typed:
            try:
                await client.kick_chat_member(chat_id, user_id, until_date=int(time() + 45))
            except RPCError as err:
                fail = await query.message.edit_text(
                    f"🛑 Failed to Kick\n<b>Error:</b>\n</code>{err}</code>"
                )
                await sleep(25)
                await fail.delete()
        else:
            await query.answer("Okda", show_alert=True)

    await query.answer()
    return
