from time import time
from imdb import IMDb
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

imdb = IMDb()

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

@Sflix.on_message(filters.group & filters.text & ~filters.edited & filters.incoming)
async def auto_detect_movie(client: Sflix, message: Message):
    if message.text.startswith("#"): return

    if len(message.text) >= 2:
        text = message.text
    else: text = ""

    search = imdb.search_movie(text, results=1)
    print(search)

    if text == search:
        buttons = [[
            InlineKeyboardButton("Leave 🧑‍🦯", callback_data="movie.leave")
            ],[
            InlineKeyboardButton("Kick 🗑️", callback_data="movie.kick")
            ],[
            InlineKeyboardButton("Ignore ✨", callback_data="movie.ignore")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text = script.MOVIE_TXT.format(message.from_user.mention),
            reply_markup = reply_markup
        )
    else:
        return

@Sflix.on_callback_query(filters.regex("^movie."))
async def who_ask_for_movie(client: Sflix, query: CallbackQuery):
    args = query.data.split(".")
    action = args[1]
    user_id = query.message.reply_to_message.from_user.id
    chat_id = int(query.message.chat.id)
    user = await client.get_users(user_id)
    user_name = user.username

    if action == "leave":
        clicked = query.from_user.id
        typed = user_id

        if int(clicked) == typed:
            try:
                await query.message.chat.ban_member(user_id, until_date=int(time() + 45))
                await sleep(3)
                await query.message.chat.unban_member(user_id)
                await query.message.edit_text(f"**User:** {user_name} **has left this group.**")
                await sleep(25)
                await query.message.delete()
            except RPCError as err:
                await query.message.edit_text(
                    f"🛑 Failed to Kick\n<b>Error:</b>\n</code>{err}</code>"
                )
                await sleep(25)
                await query.message.delete()
        else:
            await query.answer("Okda", show_alert=True)

    if action == "kick":
        admin_check = await client.get_chat_member(chat_id, user_id)
        if not ((admin_check.status == "administrator") or (admin_check.status == "creator")):
            await query.answer("Nice Try :)", show_alert=True)
            return
        try:
            await query.message.chat.ban_member(user_id, until_date=int(time() + 45))
            await sleep(3)
            await query.message.chat.unban_member(user_id)
            await query.message.edit_text(f"**User:** {user_name} **has kicked from this group.**")
            await sleep(25)
            await query.message.delete()
        except RPCError as err:
            await query.message.edit_text(
                f"🛑 Failed to Kick\n<b>Error:</b>\n</code>{err}</code>"
            )
            await sleep(25)
            await query.message.delete()

    if action == "ignore":
       admin_check = await client.get_chat_member(chat_id, user_id)
       if not ((admin_check.status == "administrator") or (admin_check.status == "creator")):
           await query.answer("Nice Try :)", show_alert=True)
           return
       await query.message.delete()
       await query.message.reply_to_message.delete()
