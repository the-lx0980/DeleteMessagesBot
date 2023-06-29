# (c) Lx 0980

from pyrogram import (
    Client,
    __version__
)

from pyrogram.enums import ParseMode
from . import (
    API_HASH,
    APP_ID,
    LOGGER,
    TG_BOT_TOKEN
)

from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from .user import User


class DeleteBot(Client):
    BOT_ID: int = None
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            name="DeleteMessagesBot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "DeleteMessages.plugins",
            },
            workers=4,
            bot_token=TG_BOT_TOKEN,
            sleep_threshold=10,
            parse_mode=ParseMode.HTML
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.BOT_ID = usr_bot_me.id
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} started! ⚡"
        )
        self.USER, self.USER_ID = await User().start()
        await self.USER.send_message(
            "Rentrox", 
            "UserBot Started!"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")

    async def iter_messages(self, chat_id: Union[int, str], limit: int, offset: int = 0) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially.
        This convenience method does the same as repeatedly calling :meth:`~pyrogram.Client.get_messages` in a loop, thus saving
        you from the hassle of setting up boilerplate code. It is useful for getting the whole chat messages with a
        single call.
        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                
            limit (``int``):
                Identifier of the last message to be returned.
                
            offset (``int``, *optional*):
                Identifier of the first message to be returned.
                Defaults to 0.
        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.
        Example:
            .. code-block:: python
                for message in app.iter_messages("pyrogram", 1, 15000):
                    print(message.text)
        """
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1
