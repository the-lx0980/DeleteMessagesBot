# (c) Lx 0980

from pyrogram import Client, filters, enums
from DeleteMessages.bot_messages import ChatMSG

@Client.on_message(filters.private & filters.command(['start', 'help']))
async def help_me(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=ChatMSG.START_TXT.format(message.from_user.first_name),
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True
    
