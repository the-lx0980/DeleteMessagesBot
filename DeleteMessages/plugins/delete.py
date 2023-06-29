# (c) Lx 0980

import os
import time

from DeleteMessages.bot import DeleteBot as Bot
from DeleteMessages import AUTH_USERS
from pyrogram import filters, enums
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from DeleteMessages.helper import get_messages
from pyrogram.errors import ChatAdminRequired

@Bot.on_message(filters.group & filters.command('cleanmedia'))
async def del_all_command_fn(client: Bot, message: Message):
    await message.delete()
    if message.from_user.id not in int(AUTH_USERS):
        return
    try:
        status_message = await client.send_message(
            chat_id=message.chat.id,
            text="<b>Deleting Messages ...</b>",
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
    except ChatAdminRequired:
        status_message = None
    try:
        await get_messages(
            client.USER,
            message.chat.id,
            0,
            status_message.id if status_message else message.id,
            []
        )
    except FloodWait as e:
        time.sleep(e.value)  
    await client.edit_message_text(
        chat_id=message.chat.id,
        text="<b>Messages Successfully Deleted</b>",
        message_id=status_message.id,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True
    )
