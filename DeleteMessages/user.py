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
    TG_USER_SESSION
)


class User(Client):

    def __init__(self):
        super().__init__(
            name="DeleteUserBot",
            in_memory=True,
            session_string=TG_USER_SESSION,
            api_hash=API_HASH,
            api_id=APP_ID,
            workers=4,
            sleep_threshold=10,
            parse_mode=ParseMode.HTML
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"{usr_bot_me} based on Pyrogram v{__version__} "
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("User stopped. Bye.")
