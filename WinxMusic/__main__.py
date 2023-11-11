import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from WinxMusic import LOGGER, app, userbot
from WinxMusic.core.call import Winx
from WinxMusic.misc import sudo
from WinxMusic.plugins import ALL_MODULES
from WinxMusic.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
        and not config.STRING6
        and not config.STRING7
        and not config.STRING8
        and not config.STRING9
        and not config.STRING10
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("WinxMusic.plugins" + all_module)
    LOGGER("WinxMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Winx.start()
    try:
        await Winx.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("WinxMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Winx.decorators()
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("WinxMusic").info("Stopping WinxMusic Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
